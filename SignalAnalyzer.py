# coding=utf-8
from Parser import *
import wave
from struct import pack


def to_wavs_bits(cod):
    counter = 0
    prev, curr = '', ''
    str_wav_bits = []
    while counter != len(cod):
        if counter != 0:
            prev = str_wav_bits[counter - 1]
            curr = cod[counter]
            if prev == '11110000' and curr == '1':
                str_wav_bits.append('11110000')
            elif prev == '00001111' and curr == '1':
                str_wav_bits.append('00001111')
            elif prev == '00001111' and curr == '0':
                str_wav_bits.append('11110000')
            elif prev == '11110000' and curr == '0':
                str_wav_bits.append('00001111')
        else:
            if cod[counter] == '1':
                str_wav_bits.append('11110000')
            else:
                str_wav_bits.append('00001111')
        counter += 1
    for i in range(0, 4):
        str_wav_bits.append('11110000')
    return ''.join(str_wav_bits)


def wav_generic(cod):
    if cod != U"нет":
        output = wave.open('generic_wav.wav', 'wb')
        output.setparams((1, 2, 38400, 1024, 'NONE', 'not compressed'))
        str_wav_bits = to_wavs_bits(cod)
        for i in range(0, len(str_wav_bits)):
            if str_wav_bits[i] == '0':
                val = -16384
                packed_value = pack('h', val)
            else:
                val = 16384
                packed_value = pack('h', val)
            output.writeframes(packed_value)
        # output.writeframes(packed_value)
        output.close()
    else:
        pass
