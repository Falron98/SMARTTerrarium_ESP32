from machine import Pin, ADC
from ili9341 import color565
from mySetup import display, unispace
from water_pump import activate_pump, deactivate_pump
from sensor import sensors_values
from buttons_mapping import button_listener
import uasyncio as asyncio
import time, sys

fsensor = 0
fsens_value = 0

def initiate_fsensor():
    global fsensor
    fsensor_pin = Pin(3, Pin.IN, Pin.PULL_UP)

    fsensor = ADC(fsensor_pin)
    fsensor.atten(fsensor.ATTN_11DB)
    
async def read_fsensor():
    global fsensor, fsens_value
    if fsensor == 0:
        initiate_fsensor()
    fsens_value = fsensor.read()

async def pump_if_water():
    global fsens_value
    try:
        for x in sensors_values:
            if sensors_values[x]["category"] == "pressure":
                pressure_value = sensors_values[x]["value"]
                min_val = sensors_values[x]["min_val"]
                print(pressure_value)
                if pressure_value > min_val:
                    activate_pump()
                else:
                    deactivate_pump()
    except Exception as e:
        sys.print_exception(e)

async def water_level():
    button = await button_listener()
    fsens_value = 0
    if button == 0:
        button = 5
    try:
        for x in sensors_values:
            if sensors_values[x]["category"] == "pressure":
                fsens_value = sensors_values[x]["value"]
                min_val = sensors_values[x]["min_val"]
                if button == 1:
                    sensors_values[x]["min_val"] = fsens_value
                    button = 5
        print(str(fsens_value))
        display.clear()
        display.draw_text(70, 128, str(fsens_value), unispace, color565(255, 255, 255))
        display.draw_text(70, 8, str("Min value: "+str(min_val)), unispace, color565(255, 255, 255))
    
    except Exception as e:
        sys.print_exception(e)
    return button
