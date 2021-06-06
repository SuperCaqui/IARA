#!/usr/bin/env python3

import sys
import signal
import multiprocessing

import microphone_recognition
import bot
import auto

sys.path.insert(0, 'snowboy/')
import snowboydecoder


interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def Hot():
    model = "iara.pmdl"

    # capture SIGINT signal, e.g., Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.4)
    print('Listening... Press Ctrl+C to exit')

    # main loop
    detector.start(detected_callback=microphone_recognition.Recog,
                interrupt_check=interrupt_callback,
                sleep_time=0.03)
                
    detector.terminate()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=bot.Start)
    p2 = multiprocessing.Process(target=auto.Auto)
    p1.start()
    p2.start()
    microphone_recognition.Ajustar()
    Hot()