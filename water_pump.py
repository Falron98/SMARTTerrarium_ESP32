from machine import Pin
import time

pin_relay = Pin(0, Pin.OUT, value=1)

def activate_pump():
    pin_relay.off()

def deactivate_pump():
    pin_relay.on()
    
