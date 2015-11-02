# coding=utf-8

from Threads import *

if __name__ == "__main__":

    listener_1 = Port_Listener_1("Listener 1")
    listener_2 = Port_Listener_2("Listener 2")
    processor = Wavs_Processor("Processor")
    player = Playing("Player")

    try:
        listener_1.start()
        listener_2.start()
        processor.start()
        player.start()
    except Exception as ex:
        print(ex)
    finally:
        listener_1.join()
        listener_2.join()
        processor.join()
        player.join()

else:
    print("Something went wrong")
