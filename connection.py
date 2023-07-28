import uasyncio as asyncio
from mqtt_async import MQTTClient, config
from WIFIconnect import show_mac, wificonnected
from sensor import read_sensor
from config_file import *
from sensor import sensors_values
import json, socket, sys, time, usocket

MQTT_id_name = MQTT_values["MQTT_ID_NAME"]
MQTT_server_ip = MQTT_values["MQTT_SERVER_IP"]
MQTT_port = MQTT_values["MQTT_PORT"]

ESP_mac = show_mac()

config['server'] = str(MQTT_server_ip)
config['port'] = int(MQTT_port)
config['client_id'] = MQTT_id_name

TCP_server_ip = TCP_values["TCP_SERVER_IP"]
TCP_port = TCP_values["TCP_PORT"]
writer = None

connected = False
tcp_connect = False

all_sensors_array = []

async def sensors_array():
    global all_sensors_array, sensors_values, ESP_mac
    
    
    all_sensors_array = []
    
    for sensor_id, sensor_data in sensors_values.items():
        sensor_template = {
            "mac_address": str(ESP_mac),
            "pin_number": sensor_id,
            "value": sensor_data['value']
        }
        all_sensors_array.append(sensor_template)
            


async def tcp_connection():
    global tcp_connect, writer, ESP_mac
    
    try:
        if not tcp_connect:
            
            print("Connecting to TCP server")
            reader, writer = await asyncio.open_connection(TCP_server_ip, TCP_port)
            tcp_connect = True
            print("Connected to TCP server")
            await tcp_send_data(str(ESP_mac))
            print("Handshake made")

        while True and tcp_connect:
            try:
                print("Receiving data")
                data = await reader.read(8)  # Adjust buffer size as per your needs
                
                if data == "request":
                    print("Sending config")
                
                # Process received data
                print("Received data:", data.decode())
                
            except Exception as e:
                sys.print_exception(e)
            
            # Yield control to the event loop
            await asyncio.sleep(0)

        print("Disconnected from server")
    
    except Exception as e:
        sys.print_exception(e)

async def tcp_send_data(data):
    global tcp_connect, writer

    try:
        if tcp_connect:
            try:
                data = data.encode("utf-8")
            except Exception as e:
                pass
            writer.write(data)
            print(len(data))
            await writer.drain()
            print("Data sent successfully!")
        else:
            print("Not connected to the server. Cannot send data.")

    except Exception as e:
        sys.print_exception(e)
    


async def connect_mqtt():
    global client, connected
    while True:
        if not connected:
            try:
                print("Starting connection", config['server'], config['port'])
                client = MQTTClient(config)
                
                
                await client.connect()
                
                
                connected = True
                
                
            except Exception as e:
                sys.print_exception(e)
            
            await asyncio.sleep(2)
        else:
            break


async def send_sensor_data():
    global connected
    global client
    global all_sensors_array

    
    if connected:
        
        try:
            message_payload = json.dumps(all_sensors_array)
            await client.publish("ESP32", message_payload)
        
        except Exception as e:
            sys.print_exception(e)

    await asyncio.sleep(0.1)
