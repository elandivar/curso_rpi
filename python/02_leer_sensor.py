import Adafruit_DHT as dht
h,t=dht.read_retry(dht.DHT22,4)
print('Temperatura={0:0.1f}*C Humedad={1:0.1f}%'.format(t,h))
