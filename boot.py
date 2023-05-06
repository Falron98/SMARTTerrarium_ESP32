# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

from WIFIconnect import connect_to_network
from esp32_usage import print_usage
from logo import start_logo, mac_image, qr_code
from connection import send_sensor_data
from lcd_data import show_sensor_data, sensor_array
from sensor import read_sensor
from buttons_mapping import click_listener, button_listener
import uasyncio as asyncio
import time

async def main():
    #start_logo()
    connect_to_network()
    #print_usage
    button = 0
    while True:
        print(button)
        if button == 4:
            print('clicked')
            mac_image()
            qr_code()
            button = 0
        if button == 3:
            print('clicked')
            values = await asyncio.gather(button_listener(), sensor_array())
            button = values[0]
        if button == 2:
            print('clicked')
            values = await asyncio.gather(button_listener(), show_sensor_data())
            button = values[0]
        if button == 1:
            print('clicked')
            start_logo()
            button = 0
        if button == 0:
            value = await read_sensor()
            values = await asyncio.gather(button_listener(), send_sensor_data(value))
            button = values[0]
            await asyncio.sleep(1)
        
if __name__ == "__main__":
    asyncio.run(main())
    
