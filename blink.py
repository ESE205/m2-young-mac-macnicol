import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
import sys                 # Import Arvg

ITER_COUNT = 5  
pin1 = 40                  # Pin for LED Output
pin2 = 16                  # Pin for input

GPIO.setup(pin2, GPIO.IN)
GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
if len(sys.argv)>1:  
   ITER_COUNT = int(sys.argv[1])    #If user enters a command line arg for iter.

if GPIO.input(pin2):
   while ITER_COUNT > 0: # Run ITER_COUNT times
      ITER_COUNT -= 1 # Decrement counter
      GPIO.output(pin1, GPIO.HIGH) # Turn on
      sleep(1)                     # Sleep for 1 second
      GPIO.output(pin1, GPIO.LOW)  # Turn off
      sleep(1)                     # Sleep for 1 second
   GPIO.cleanup()

