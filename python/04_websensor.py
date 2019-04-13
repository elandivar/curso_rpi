from flask import Flask
import Adafruit_DHT as dht
h,t=dht.read_retry(dht.DHT22,4)
app=Flask(__name__)

@app.route('/')
def hello():
    return 'Compu del Instructor<br>Temperatura={0:0.1f}*C Humedad={1:0.1f}%'.format(t,h)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
