import sys
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime

GPIO.setmode(GPIO.BOARD)

blinkPeriod = float(sys.argv[1])
progDuration = float(sys.argv[2])

DEBUG = False
if '-debug' in sys.argv:
   DEBUG = True

numLoops = int(progDuration / blinkPeriod)

inputPin = 16
ledPin = 40

GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(inputPin, GPIO.IN)

f = open("m2Prelab.txt","w")

for i in range(numLoops):
   if GPIO.input(inputPin):
      if GPIO.input(ledPin):
         GPIO.output(ledPin, GPIO.LOW)
         f.write("\tSWITCH: ON\n\tLED: OFF\n\n")
      else:
         GPIO.output(ledPin, GPIO.HIGH)
         f.write("\tSWITCH: ON\n\tLED: ON\n\n")
   else:
      if GPIO.input(ledPin):
         GPIO.output(ledPin, GPIO.LOW)
         f.write("\tSWITCH: OFF\n\tLED: OFF\n\n")

   if DEBUG:
      if GPIO.input(inputPin):
         switchState = 'ON'
      else:
         switchState = 'OFF'

      now = datetime.now()
      print(f'Current time: {now.time()} \t Number of iterations: {i+1} \t Switch state: {switchState}') 
 
   sleep(blinkPeriod)

GPIO.cleanup()
f.close()
