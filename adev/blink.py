import RPi.GPIO as GPIO

with open("status.txt", "w") as statfile:
    statfile.write("True")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

from time import sleep

for i in range(100):
    GPIO.output(11, i % 2)
    sleep(0.1)


GPIO.output(11, False)
