from gpiozero import LED, Button, Buzzer
from time import sleep
import os

LED1 = LED(17)
LED2 = LED(18)
LED3 = LED(27)
LED4 = LED(22)
LED5 = LED(25)
LED6 = LED(12)
LED7 = LED(13)
LED8 = LED(19)

SW1 = Button(21)
SW2 = Button(16)
SW3 = Button(20)

BUZZER = Buzzer(26)

NONE = 0
DECREASE = 1
INCREASE = 2
ALL_OFF = 9
ALL_ON = 10

def beep(times, sec):
  for x in range(times):
    BUZZER.on()
    sleep(sec)
    BUZZER.off()
    sleep(sec)

def led(ledNumber):
  if ledNumber == 1:
    LED1.on()
  else:
    LED1.off()

  if ledNumber == 2:
    LED2.on()
  else:
    LED2.off()

  if ledNumber == 3:
    LED3.on()
  else:
    LED3.off()

  if ledNumber == 4:
    LED4.on()
  else:
    LED4.off()

  if ledNumber == 5:
    LED5.on()
  else:
    LED5.off()

  if ledNumber == 6:
    LED6.on()
  else:
    LED6.off()

  if ledNumber == 7:
    LED7.on()
  else:
    LED7.off()

  if ledNumber == 8:
    LED8.on()
  else:
    LED8.off()

  if ledNumber == ALL_OFF:
    LED1.off()
    LED2.off()
    LED3.off()
    LED4.off()
    LED5.off()
    LED6.off()
    LED7.off()
    LED8.off()
  elif ledNumber == ALL_ON:
    LED1.on()
    LED2.on()
    LED3.on()
    LED4.on()
    LED5.on()
    LED6.on()
    LED7.on()
    LED8.on()

mode = NONE
ledPosition = 0

led(ALL_ON)
beep(1, 0.1)
led(ALL_OFF)

try:
  while True:
    if SW1.is_pressed and mode != DECREASE:
      beep(2, 0.07)
      mode = DECREASE

    elif SW2.is_pressed and SW3.is_pressed:
      sleep(0.5)
      for loop in range(3):
        led(ALL_ON)
        BUZZER.on()
        sleep(0.2)
        led(ALL_OFF)
        BUZZER.off()
        sleep(0.2)
      sleep(1)
      os.system("sudo shutdown -h now")
      
    elif SW2.is_pressed and mode != INCREASE:
      beep(2, 0.07)
      mode = INCREASE

    elif SW3.is_pressed and mode != NONE:
      beep(1, 0.07)
      mode = NONE

    if mode == INCREASE:
      if ledPosition < 8:
        ledPosition = ledPosition + 1
      else:
        ledPosition = 0

    elif mode == DECREASE:
      if ledPosition > 0:
        ledPosition = ledPosition - 1
      else:
        ledPosition = 8

    led(ledPosition)

    sleep(0.05)

except KeyboardInterrupt:
  led(ALL_OFF)
