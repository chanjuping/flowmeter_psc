import RPi.GPIO as GPIO
import time, sys
GPIO.setmode(GPIO.BOARD)
inpt = 13
GPIO.setup(inpt,GPIO.IN)
reading2 = 0
time_start = 0
time_end = 0
duration = 0

try:
        reading1 = GPIO.input(inpt)
        print(reading1)

except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
