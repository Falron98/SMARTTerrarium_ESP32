from machine import Pin, ADC
from config_file import *
import uasyncio as asyncio
import urandom

adc_pin = Pin(BUTTON_ADC_PIN, Pin.IN, Pin.PULL_DOWN)
adc = ADC(adc_pin)
adc.atten(adc.ATTN_11DB)
min_moisture=1600
max_moisture=8191

async def read_sensor():
    #reading = adc.read()
    reading = urandom.randint(3000, 6000)
    m = (max_moisture-reading)*100/(max_moisture-min_moisture)
    moisture = '{:.1f} %'.format(m)
    return round(m)

