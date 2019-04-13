from flask import Flask
import Adafruit_DHT as dht
import RPi.GPIO as gpio
import time

h,t=dht.read_retry(dht.DHT22,4)
app=Flask(__name__)

gpio.setmode(gpio.BCM)
led = 22

@app.route('/')
def hello():
    global t
    global h
    temphum = print('Temp={0:0.1f} {1:0.1f}'.format(3,5))
    salida = (temphum)
    return salida



if __name__ == '__main__':
    app.run(host='0.0.0.0')
