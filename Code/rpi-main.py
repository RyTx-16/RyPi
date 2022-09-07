#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import socket 

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # For UDP

#list = [4, 16, 23, 24, 17, 27, 22, 26]
list = [6, 12, 13, 16, 19, 20, 21, 26]

prev = 0

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for e in list:
        GPIO.setup(e, GPIO.IN,  GPIO.PUD_DOWN)
    #print("Pins Ready")

def send_msg(n, sock):
    msg = n.encode('utf-8')
    sock.sendto(msg,("192.168.1.180", 12345))

def algo():
    for e in list:
        input = GPIO.input(e)
        if ((not prev) and input == GPIO.HIGH): 
            send_msg(str(e), s)
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
