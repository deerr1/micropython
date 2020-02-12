import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connect"+str(rc))


if __name__ == "__main__":
    topic='mes'
    msg=('off')
    client = mqtt.Client()
    client.on_connect = on_connect
    client.username_pw_set("tjtmgqai", "JAokZEKyi3PU")
    client.connect('hairdresser.cloudmqtt.com', 15979, 60)
    client.publish(topic, msg)
    client.loop_forever()
    

