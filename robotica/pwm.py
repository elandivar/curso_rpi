import sys
import time
import RPi.GPIO as GPIO

GPIO.cleanup()

PIN_avanz=26

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_avanz, GPIO.OUT)

def avanzar_pwm(segundos, dc):
    p = GPIO.PWM(PIN_avanz, 4000)
    p.start(dc)
    print("Motor avanzando ", dc, "%")
    time.sleep(segundos)
    p.stop()

while (1):
    for dc in range (0, 101, 5):
        dc_mod = dc/10
        avanzar_pwm(1, dc_mod) 

GPIO.cleanup()
