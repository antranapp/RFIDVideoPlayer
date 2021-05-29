#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import sys

reader = SimpleMFRC522.SimpleMFRC522()

text = sys.argv[1]

try:

    print('Scan Card')
    print("New data: %s" % text)

    print("Now place your tag to write")

    reader.write(text)
    print("Written")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nClean Exit")
