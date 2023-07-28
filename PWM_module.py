from machine import Pin, PWM
from config_file import PWM_values
import time

pwm_bulb = PWM(Pin(int(PWM_values["PWM_PIN"])), 5000)

# pwm_bulb.duty
# 0 - off
# 15, 16 - low
# 17 - med
# 18 - high

def change_intensity(volume):
    if volume == "very low":
        pwm_bulb.duty(15)
    elif volume == "low":
        pwm_bulb.duty(16)
    elif volume == "medium":
        pwm_bulb.duty(17)
    elif volume == "high":
        pwm_bulb.duty(18)
    else:
        pwm_bulb.duty(0)