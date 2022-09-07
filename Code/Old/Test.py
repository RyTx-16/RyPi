#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

list = [21, 4] #21

#GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)

#while True:
 #   button_state = GPIO.input(button)
  #  if button_state == GPIO.HIGH:
   #   print ("1")
    #  time.sleep(0.5)
      
prev = 0

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for e in list:
        GPIO.setup(e, GPIO.IN, GPIO.PUD_DOWN)
    #print("Pins Ready")

def algo():
    for e in list:
        input = GPIO.input(e)
        if ((not prev) and input == GPIO.HIGH): 
            #send_msg(str(e), s)
            print(e)
            time.sleep(1)
            
if __name__ == "__main__":
    setup()
    time.sleep(1)
    print("Program starting...")
    try:
        while True:
            algo()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()