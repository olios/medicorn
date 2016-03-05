import RPi.GPIO as GPIO
import time
import math
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
p = GPIO.PWM(13, 3000)  # channel=12 frequency=50Hz
p.start(0)
max = 100.0
p.ChangeDutyCycle(100)

# hasici
try:
    counter = 1
    while 1:
        for dc in range(0, 100, 1):
            freq = 440
            if counter % 2 == 0:
                freq = freq * 1.333  # perfect quart
            p.ChangeFrequency(freq)
            time.sleep(0.3)
            counter += 1
            p.ChangeDutyCycle(dc)
        for dc in range(100, -1, -1):
            freq = 440
            if counter % 2 == 0:
                freq = freq * 1.333  # perfect quart
            p.ChangeFrequency(freq)
            time.sleep(0.3)
            counter += 1
            p.ChangeDutyCycle(dc)
except KeyboardInterrupt:
    pass

try:
    counter = 1
    while 1:
        for dc in range(0, 100, 1):
            freq = math.fabs(math.sin(counter/max))*5000
            print(freq)
            p.ChangeDutyCycle(dc)
            p.ChangeFrequency(freq+1)
            counter += 10
            time.sleep(0.1)
            counter = counter%max
        for dc in range(100, -1, -1):
            freq = math.fabs(math.sin(counter/max))*5000
            print(freq)
            p.ChangeDutyCycle(dc)
            p.ChangeFrequency(freq+1)
            counter += 10
            time.sleep(0.1)
            counter = counter%max
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
