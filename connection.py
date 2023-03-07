
from umqtt.simple import MQTTClient

server_ip = "0.0.0.0"
port = 8000

print("Connecting...")
client = MQTTClient("ESP32", server_ip, port=port)
client.connect()

while True:
    print("Pętla start")
    sensor_value = 32
    client.publish("esp32/sensors/sensor_1", str(sensor_value))
    print("Wysłano dane z czujnika 1: " + str(sensor_value))
    time.sleep(5)