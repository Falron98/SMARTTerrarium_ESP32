from machine import Pin, ADC
from config_file import *
import uasyncio as asyncio
import urandom
import dht
import time
import sys


sensors_values = {}

first_start = True

for x in SENSORS:
    sensors_values[x['pin_number']] = {'category' : x['category'], 'min_val' : x['min_val'],
                                      'max_val' : x['max_val'], 'value' : 0, 'pin_object' : ''}
    
async def read_sensor():
    global first_start
    if first_start == True:
        define_sensor()
        first_start = False
    for x in sensors_values:
        if len(str(x)) > 2:
            time.sleep(1)
            try:
                sensors_values[x]['pin_object'].measure()
            except Exception as e:
                sensors_values[x]['value'] = 0
                #sys.print_exception(e)
                continue
            if sensors_values[x]['category'] == 'temperature':
                try:
                    sensors_values[x]['value'] = int(sensors_values[x]['pin_object'].temperature())
                except Exception as e:

                    sys.print_exception(e)
                    sensors_values[x]['value'] = 0
            elif sensors_values[x]['category'] == 'humidity':
                try:
                    sensors_values[x]['value'] = int(sensors_values[x]['pin_object'].humidity())
                except Exception as e:

                    sys.print_exception(e)
                    sensors_values[x]['value'] = 0

        else:
            if sensors_values[x]['category'] == 'pressure':
                try:
                    sensors_values[x]['pin_object'].atten(sensors_values[x]['pin_object'].ATTN_11DB)
                    sensors_values[x]['value'] = int(sensors_values[x]['pin_object'].read())
                except Exception as e:

                    sys.print_exception(e)
                    sensors_values[x]['value'] = 0
            else:                    
                try:
                    sensors_values[x]['value'] = int(sensors_values[x]['pin_object'].value())
                except Exception as e:

                    sys.print_exception(e)
                    sensors_values[x]['value'] = 0
            

def define_sensor():
    dht_pin = None
    try:
        for y in sensors_values:
            if len(str(y)) > 2:
                if dht_pin is None:
                    sensors_values[y]['pin_object'] = dht.DHT22(Pin(int(str(y)[0])))
                    dht_pin = sensors_values[y]['pin_object']
                else:
                    sensors_values[y]['pin_object'] = dht_pin
                    dht_pin = None
            elif sensors_values[y]['category'] == 'pressure':
                sensors_values[y]['pin_object'] = ADC(Pin(y, Pin.IN, Pin.PULL_UP))
            else:
                sensors_values[y]['pin_object'] = Pin(y, Pin.OUT)
    except Exception as e:

        sys.print_exception(e)
    
