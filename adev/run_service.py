import sys

import subprocess
import shlex
import time
import math
import RPi.GPIO as GPIO

from threading import Thread


def main(args):
    method = args[1]
    fire = False
    try:
        fire = bool(args[2])
    except:
        pass
    try:
        print(method)
        if method == "mplay":
            mplay()
        elif method == "piezo":
            piezo(fire)
        elif method == "start":
            start(fire)
        elif method == "stop":
            stop()
        elif method == "blink":
            blink()
        elif method == "light":
            light()
        elif method == "status":
            status()
        elif method == "spiezo":
            stop_piezo()
        else:
            pass
    except KeyboardInterrupt as ex:
        print("Terminated by user.")
    except SystemExit as ex:
        print("Finished. Exiting")


def start(fire):
    with open("status.txt", "w") as statfile:
        statfile.write("True")
    for f in [blink, piezo]:
        Thread(target=f,args=(fire,)).start()


def stop():
    print("start of stop")
    with open("status.txt", "w") as statfile:
        statfile.write("False")
    #for f in [ dim, stop_piezo]:
    #    Thread(target=f).start()
    dim()
    stop_piezo()

def stop_play():
    pass


def mplay(fire=False):
    if fire:
        subprocess.call(shlex.split("/usr/bin/mplayer siren.mp3"))
    else:
        subprocess.call(shlex.split("/usr/bin/mplayer siren.mp3"))

def dim():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, False)

def status():
    with open("status.txt", "r") as status:
        r = status.read()
        print(r)

def light():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, True)

def blink(fire=False):
    if fire:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)

        for i in range(100):
            GPIO.output(11, i % 2)
            time.sleep(0.1)

        GPIO.output(11, False)
    else:
        light()

def stop_piezo():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)
    p = GPIO.PWM(13, 3000)  # channel=12 frequency=50Hz
    p.ChangeDutyCycle(0)
    p.stop()
    GPIO.cleanup()
    print("piezo stop")


def piezo(fire=True):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)
    p = GPIO.PWM(13, 3000)  # channel=12 frequency=50Hz
    p.start(0)
    max = 100.0
    p.ChangeDutyCycle(100)

    try:
        counter = 1
        while 1:
            for dc in range(0, 100, 1):
                if fire:
                    fire_siren(p, dc, counter, max)
                else:
                    health_siren(p, dc, counter, max)
                print(counter)
            for dc in range(100, -1, -1):
                if fire:
                    fire_siren(p, dc, counter, max)
                else:
                    health_siren(p, dc, counter, max)
    except KeyboardInterrupt:
        pass

    p.stop()
    GPIO.cleanup()

def fire_siren(p, dc, counter, max):
    freq = 440
    if counter % 2 == 0:
        freq = freq * 1.333  # perfect quart
    p.ChangeFrequency(freq)
    time.sleep(0.3)
    counter += 1
    p.ChangeDutyCycle(dc)

def health_siren(p, dc, counter, max):
    freq = math.fabs(math.sin(counter/max))*5000
    p.ChangeDutyCycle(dc)
    p.ChangeFrequency(freq+1)
    counter += 10
    time.sleep(0.1)
    counter = counter%max

if __name__ == "__main__":
    main(sys.argv)

