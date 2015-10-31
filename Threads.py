# coding=utf-8

import threading
import Queue
import pyaudio
from struct import *
from SignalAnalyzer import *

toRun = False
split_left = []
split_right = []

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 38400
RECORD_SECS = 0.18

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

mut_port = threading.Lock()
mut_buffer = threading.Lock()
buffer = Queue.Queue()


class Port_Listener_1(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.stream = stream
        self.frames = []

    def run(self):
        global toRun
        while True:
            if not toRun:
                try:
                    mut_port.acquire()
                    for i in range(0, int(RATE / CHUNK * RECORD_SECS)):
                        data = stream.read(CHUNK)
                        self.frames.append(data)
                    mut_port.release()
                    mut_buffer.acquire()
                    buffer.put(self.frames)
                    self.frames = []
                    mut_buffer.release()
                    #                print("Thread %s done" % self.name)
                    #                print("Buf len_1 %s from %s" % (buffer_wav_part_1.qsize(), self.name))
                except Exception as ex:
                    print(ex)
                toRun = True
            else:
                pass


class Port_Listener_2(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.stream = stream
        self.frames = []

    def run(self):
        global toRun
        while True:
            if toRun:
                try:
                    mut_port.acquire()
                    for i in range(0, int(RATE / CHUNK * RECORD_SECS)):
                        data = stream.read(CHUNK)
                        self.frames.append(data)
                    mut_port.release()
                    mut_buffer.acquire()
                    buffer.put(self.frames)
                    self.frames = []
                    mut_buffer.release()
                    #                print("Thread %s done" % self.name)
                    #                print("Buf len_2 %s from %s" % (buffer_wav_part_2.qsize(), self.name))
                except Exception as ex:
                    print(ex)
                toRun = False
            else:
                pass


def buffer_processing(buffer):
    whole_list = []
    counter, item_to_decode = 0, ''
    try:
        for i in range(0, len(buffer)):
            item_to_decode += buffer[i]
            counter += 1
            if counter % 2 == 0 and counter != 0:
                (p) = unpack('h', item_to_decode)
                if p[0] >= 0:
                    whole_list.append(str(1))
                else:
                    whole_list.append(str(0))
                item_to_decode = ''
            else:
                continue

    except Exception as ex:
        print(ex)

    return whole_list


cnt_err = 0


class Wavs_Processor(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.list_bits = []

    def run(self):
        global list_split, lst_str, cnt_err
        while True:
            if not buffer.empty():
                try:
                    list_split, lst_str = [], ""
                    mut_buffer.acquire()
                    self.list_bits = buffer_processing(b''.join(buffer.get()))
                    mut_buffer.release()

                    # self.list_left = self.list_left + list_left_split
                    self.list_bits = list_split + self.list_bits

                    # left_str, list_left_split = correction(self.list_left)
                    # self.list_left = get_templates(left_str)
                    # left_str = to_string_converter(self.list_right)

                    right_str, list_split = correction(self.list_bits)
                    self.list_bits = get_templates(right_str)

                    right_str = to_string_converter(self.list_bits)

                    lst_right, lst_right_desc, lst_bad, lst_bad_desc = templates_finder(right_str)

                    right_str, cnt_err = codogramm_counter(lst_right, lst_right_desc, cnt_err)

                    # print("Right channel : %s" % right_str)

                    # output_mutx.acquire()
                    # buffer_to_output.put(right_str)
                    # output_mutx.release()

                    wav_file_mutx.acquire()
                    wav_generic(right_str.split("*")[1])
                    wav_file_mutx.release()

                    print(right_str.split("*")[1])

                except Exception as ex:
                    print(ex.message)
            else:
                pass


buffer_to_output = Queue.Queue()
output_mutx = threading.Lock()
wav_file_mutx = threading.Lock()

class Playing(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.output = ""

    def run(self):
        str_cod = ''
        while True:
            if not buffer_to_output.empty():
                try:
                    wav_file_mutx.acquire()
                    wf = wave.open('generic_wav.wav', 'rb')
                    p_o = pyaudio.PyAudio()
                    stream_output = p_o.open(format=p_o.get_format_from_width(wf.getsampwidth()),
                                             channels=wf.getnchannels(),
                                             rate=wf.getframerate(),
                                             output=True)
                    data = wf.readframes(1024)
                    wav_file_mutx.release()
                    while True:
                        stream.write(data)
                        data = wf.readframes(1024)
                except Exception as ex:
                    print(ex)
                finally:
                    stream_output.stop_stream()
                    stream_output.close()
                    p_o.terminate()
            else:
                pass
