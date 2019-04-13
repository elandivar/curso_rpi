import RPi.GPIO as gpio
import time

led = 22
gpio.setmode(gpio.BCM)

gpio.setup(led, gpio.OUT)
gpio.output(led, gpio.HIGH)
time.sleep(1)
gpio.output(led, gpio.LOW)

gpio.cleanup()
