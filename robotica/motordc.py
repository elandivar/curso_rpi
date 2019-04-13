import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.cleanup()

PIN_avanz=26
PIN_retro=20

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_avanz, GPIO.OUT)
GPIO.setup(PIN_retro, GPIO.OUT)

def avanzar(x):
    GPIO.output(PIN_avanz, GPIO.HIGH)
    print("Motor avanzando")
    time.sleep(x)
    GPIO.output(PIN_avanz, GPIO.LOW)

def retroceder(x):
    GPIO.output(PIN_retro, GPIO.HIGH)
    print("Motor retrocediento")
    time.sleep(x)
    GPIO.output(PIN_retro, GPIO.LOW)

while (1):
    avanzar(5)
    retroceder(5)
    
GPIO.cleanup()
