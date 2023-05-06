import network
from ili9341 import color565
from mySetup import display, unispace
import time
import binascii


network.WLAN(network.AP_IF).active(False)
sta_if = network.WLAN(network.STA_IF)

def connect_to_network():
    first_time_conn = 0
    
    
    if not sta_if.isconnected():
        first_time_conn = 1
        print('Connecting to network...')
        try:
            display.draw_text(0, 0, 'Connecting to network...', unispace, color565(255, 128, 0))
        except Exception as e:
            print ("No LCD found")
            
        try:
            sta_if.active(True)
            sta_if.connect("Redmi", "12345678")
        except Exception as e:
            print(e)

        while not sta_if.isconnected():
            pass
        try:
            display.clear()
        except Exception as e:
            print ("No LCD found")

    try:
        display.draw_text(0, 0, 'Succesfuly connected', unispace, color565(255, 128, 0))
    except Exception as e:
        print ("No LCD found")
    
    time.sleep(3)
    if first_time_conn == 1:
        try:
            display.clear()
        except Exception as e:
            print ("No LCD found")

        line_y = 0
        net_config = sta_if.ifconfig()
        try:
            display.draw_text(0, 0, 'Network config:', unispace, color565(255, 128, 0))
        except Exception as e:
            print ("No LCD found")
        print('Network config:', net_config)

        for i in net_config:
            line_y += 24
            time.sleep(1)
            try:
                display.draw_text(0, line_y, i, unispace, color565(255, 128, 0))
            except Exception as e:
                print ("No LCD found")
        time.sleep(1)
    first_time_connect = 0
    try:
        display.clear()
    except Exception as e:
        print ("No LCD found")

def show_mac():
    mac_address = sta_if.config('mac')
    
    mac_address = binascii.hexlify(mac_address, ':').decode()
    return mac_address
    