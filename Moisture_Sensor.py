#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIOchannel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIOchannel, GPIO.IN)

def getMoisture(GPIOchannel):
    if GPIO.input(GPIOchannel):
        print("Low Water Level")
    else:
        print("High Water Level")
        
GPIO.add_event_detect(GPIOchannel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(GPIOchannel, getMoisture)

while True:
    time.sleep(1)
