from machine import Pin, ADC
import uasyncio as asyncio
import time

# Define the GPIO pins used by each button
BUTTON_PIN = Pin(6, Pin.IN, Pin.PULL_DOWN)

# Create Pin objects for each button
buttons_mode = ADC(BUTTON_PIN)
buttons_mode.atten(buttons_mode.ATTN_11DB)
buttons_mode_val = buttons_mode.read()

button = 0

# Read the state of each button

async def click_listener():
    val = BUTTON_PIN.value
    if BUTTON_PIN.value == 1:
        return val
    else:
        return val

async def button_listener():
    buttons_mode_val = buttons_mode.read()
    if 1000 < buttons_mode_val < 2000:
        button = 1
    elif 2000 < buttons_mode_val < 3000:
        button = 2
    elif 3000 < buttons_mode_val < 4000:
        button = 3
    elif 5000 < buttons_mode_val < 6000:
        button = 4
    elif 6000 < buttons_mode_val < 7000:
        button = 5
    elif 7000 < buttons_mode_val < 8000:
        button = 6
    else:
        button = 0
    
    return button

