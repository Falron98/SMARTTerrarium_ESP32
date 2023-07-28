# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)


from config_file import load_ftp_files
from WIFIconnect import connect_to_network
from connection import send_sensor_data, sensors_array, connect_mqtt, tcp_connection
from lcd_data import show_sensor_data, sensor_array, sensors_dict_data_append
from sensor import read_sensor
from buttons_mapping import button_listener
from pressure_plate import pump_if_water, read_fsensor, water_level
from PWM_module import change_intensity
from alerts import check_for_alerts
from ftp_server import start_ftp
from configuration import first_config
import uasyncio as asyncio
import time

async def main():
    button = 0
    while True:
        print(button)
        await read_sensor()
        await sensors_dict_data_append()
        await sensors_array()
        await pump_if_water()
        await send_sensor_data()
        await check_for_alerts()
        if button == 5:
            print('clicked')
            values = await asyncio.gather(water_level())
            button = values[0]
        if button == 4:
            print('clicked')
            first_config()
            await start_ftp()
            button = 0
        if button == 3:
            print('clicked')
            values = await asyncio.gather(sensor_array())
            button = values[0]
        if button == 2:
            print('clicked')
            values = await asyncio.gather(show_sensor_data())
            button = values[0]
        if button == 1:
            print('clicked')
            start_logo()
            button = 0
        if button == 0 or button == 6:
            values = await asyncio.gather(button_listener())
            button = values[0]
        
        
if __name__ == "__main__":
    load_ftp_files()
    connect_to_network()
    time.sleep(5)
    event_loop = asyncio.get_event_loop()
    event_loop.create_task(main())
    event_loop.create_task(connect_mqtt())
    event_loop.create_task(tcp_connection())
    event_loop.run_forever()
 
    
