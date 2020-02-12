from umqtt.simple import MQTTClient
from machine import Pin
import network
import ujson

def sub_cb(topic, msg):
    print((topic, msg))
    msg=msg.decode("utf-8")
    print(msg)
    
    if msg == 'on':
        Pin (2, Pin.OUT) .value (0)
    else:
        Pin (2, Pin.OUT) .value (1)

router = network.WLAN(network.STA_IF)
router.active(True)
router.connect('RT-GPON-D7D6','4CVEKT4C')
print('connect')

server = 'hairdresser.cloudmqtt.com'
client_id = 'esp'
topic = b'mes'
user='tjtmgqai'
password = 'JAokZEKyi3PU'
port = 15979


client = MQTTClient(client_id, server, port, user, password)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic)

while True:
   client.wait_msg()

