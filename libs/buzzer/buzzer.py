import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

buzzTime = 0.5
buzzDeplay = 1
buzzPin = 27

GPIO.setup(buzzPin, GPIO.OUT)

try:
    while True:
        GPIO.output(buzzPin, True)
        print("beep")
        sleep(buzzTime)
        GPIO.output(buzzPin, False)
        print("no beep")
        sleep(buzzDeplay)
finally:
    GPIO.cleanup()
    print("done")
