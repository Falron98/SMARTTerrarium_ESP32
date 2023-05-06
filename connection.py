import uasyncio as asyncio
from umqtt.simple import MQTTClient
from sensor import read_sensor
from config_file import *

id_name = MQTT_ID_NAME
server_ip = MQTT_SERVER_IP
port = MQTT_PORT

def connect_mqtt():
    try:
        print("Starting connection")
        client = MQTTClient(id_name, server_ip, port=port)
        return client
    except Exception as e:
        return e
    

async def send_sensor_data(sensor_value):
    
    client = connect_mqtt()
    
    client.connect()

    print("Sending value")
    client.publish("esp32/sensors/sensor_1", str(sensor_value))
    
    client.disconnect()

    await asyncio.sleep(0.1)
