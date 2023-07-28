import uasyncio as asyncio
from umqtt.simple import MQTTClient
from sensor import read_sensor

server_ip = "192.168.192.186"
port = 6330

print('starting')
def send_sensor_data():
    
    client = MQTTClient("ESP32", server_ip, port=port)
    client.connect()
    
    sensor_value = 123
    client.publish("esp32/sensors/sensor_1", str(sensor_value))
    print("Sent")

send_sensor_data()
