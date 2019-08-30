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
        time.start = time.time()
        reading1 = GPIO.input(inpt)
        while(reading1 == reading2):
                reading1 = GPIO.input(inpt)
                if reading1 != reading2:
                        time_end = time.time()
                        duration = time_end - time_start
                        print(duration)

                        #if duration >=  5:
                                #None
                                #print("no flow")

                #print(reading1)
                #print(duration)
                reading2 = reading1
                #print(time_start)

except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()

