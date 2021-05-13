from gpiozero import Button
from signal import pause
import time  
import os  

def shutdown():
    print("Shutdown")

def restart():
    print("Restart")

button = Button(21)
press_time = 0
release_time = 0

def on_pressed():
    global press_time
    print("Pressed")
    press_time = time.time()

def on_released():
    print("Released")
    release_time = time.time()
    pressing_duration = release_time - press_time
    print("duration = ", release_time, press_time,  pressing_duration)
    if pressing_duration < 2:
        print("should restart")
        os.system("sudo shutdown -r now")
    else:
        print("should shutdown")
        os.system("sudo shutdown -h now")

button.when_pressed = on_pressed
button.when_released = on_released

while True:
    time.sleep(1)

button.close()
