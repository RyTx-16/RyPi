#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import socket 

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # For UDP
print("Socket Ready")

def GPIO_Setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    GPIO.setup(16, GPIO.IN)
    GPIO.setup(23, GPIO.IN)
    GPIO.setup(24, GPIO.IN)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(27, GPIO.IN)
    GPIO.setup(22, GPIO.IN)
    GPIO.setup(26, GPIO.IN)
    print("Pins Ready")

def send_msg(n, sock):
    msg = n.encode('utf-8')
    sock.sendto(msg,("100.71.209.169", 12345))
    
prev = 0
GPIO_Setup()

list = [4, 16, 23, 24, 17, 27, 22, 26]

def algo():
    for e in list:
        input = GPIO.input(e)
        if ((not prev) and input): 
            send_msg(str(e), s)
            print(e)
            time.sleep(1)


try:
    while True:
        """
        input = GPIO.input(4)
        if ((not prev) and input):
            send_msg("3", s)
            time.sleep(.5) # Key Debouncing
        prev = input
        input = GPIO.input(16)
        if ((not prev) and input):
            send_msg("4", s)
            time.sleep(.5) 
        prev = input
        input = GPIO.input(23)
        if ((not prev) and input):
            send_msg("1", s)
            time.sleep(.5) 
        input = GPIO.input(24)
        if ((not prev) and input):
            send_msg("2", s)
        time.sleep(.5)
        input = GPIO.input(17)
        if ((not prev) and input):
            send_msg("5", s)
            time.sleep(.5)
        input = GPIO.input(27)
        if ((not prev) and input):
            send_msg("6", s)
            time.sleep(.5)
        input = GPIO.input(22)
        if ((not prev) and input):
            send_msg("7", s)
            time.sleep(.5)
        input = GPIO.input(26)
        if ((not prev) and input):
            send_msg("8", s)
            time.sleep(.5) 
        """
        algo()
except KeyboardInterrupt:
    pass
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
