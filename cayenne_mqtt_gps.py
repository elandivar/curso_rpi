#!/usr/bin/env python
import cayenne.client
import time
import logging
from gps3 import gps3

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "USERNAME"
MQTT_PASSWORD  = "PASSWORD"
MQTT_CLIENT_ID = "CLIENTID"

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, 'mqtt.mydevices.com')
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883, loglevel=logging.INFO)

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        client.loop()
        client.virtualWrite(1, str(data_stream.TPV['lat']) + "," + str(data_stream.TPV['lon']) + "," + str(data_stream.TPV['alt']), "gps", "m") 
        time.sleep(10)
