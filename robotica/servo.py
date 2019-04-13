import RPi.GPIO as GPIO
import time

PIN_avanz = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_avanz, GPIO.OUT)

pwm = GPIO.PWM(PIN_avanz, 100)
pwm.start(5)

angle1=10
duty1=float(angle1)/10 + 2.5

angle2=160
duty2=float(angle2)/10 + 2.5

ck=0
while ck<=5:
    pwm.ChangeDutyCycle(duty1)
    time.sleep(1)
    pwm.ChangeDutyCycle(duty2)
    time.sleep(1)
    ck=ck+1

time.sleep(1)
GPIO.cleanup()
