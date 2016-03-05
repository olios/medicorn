import RPi.GPIO as GPIO

with open("status.txt", "w") as statfile:
    statfile.write("False")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, False)
print("False")
