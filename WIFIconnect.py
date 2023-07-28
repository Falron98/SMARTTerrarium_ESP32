import network, sys
from mySetup import display, unispace, WHITE
from config_file import WIFI_values
import time
import binascii


network.WLAN(network.AP_IF).active(False)
sta_if = network.WLAN(network.STA_IF)

MAX_CONNECTION_ATTEMPTS = 3

WIFI_SSID = WIFI_values["WIFI_SSID"]
WIFI_PASSWORD = WIFI_values["WIFI_PASSWORD"]

wificonnected = False


def connect_to_network(WIFI_SSID=WIFI_SSID, WIFI_PASSWORD=WIFI_PASSWORD):
    
    global wificonnected
    
    first_time_conn = 0
    
    if not sta_if.isconnected():
        print('Connecting to network...')

            
        for attempt in range(MAX_CONNECTION_ATTEMPTS):
            try:
                try:
                    display.draw_text8x8(0, 8, 'Connecting to network...', WHITE)
                    time.sleep(2)
                except Exception as e:
                    sys.print_exception(e)
                sta_if.active(True)
                
                sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
                
                time.sleep(5)
                
                if sta_if.isconnected():
                    print('Connected to network!')
                    wificonnected = True
                    try:
                        display.clear()
                        display.draw_text8x8(0, 8, 'Succesfuly connected', WHITE)
                    except Exception as e:
                        sys.print_exception(e)
                    
                    first_time_conn = 1
                    time.sleep(3)
                    break
                else:
                    print(f'Attempt {attempt+1} failed.')
                    try:
                        display.clear()
                        display.draw_text8x8(0, 8*(attempt+1), f'Attempt {attempt+1} failed.', WHITE)
                        time.sleep(3)
                        
                        display.clear()
                    except Exception as e:
                        sys.print_exception(e)
                    
            except Exception as e:
                print(f'Attempt {attempt+1} failed with error: {e}')
                        
                try:
                    
                    display.clear()
                    display.draw_text8x8(0, 8*(attempt+1), f'Attempt {attempt+1} failed with error', WHITE)
                    
                    time.sleep(3)
                    display.clear()
                except Exception as d:
                    sys.print_exception(e)
        

        
    else:
        print('WIFI connected')
        wificonnected = True
        try:
            display.draw_text8x8(0, 8, 'WIFI connected', WHITE)
            
            time.sleep(5)
            
            display.clear()
        except Exception as e:
            sys.print_exception(e)

        
    if first_time_conn == 1:
        try:
            display.clear()
        except Exception as e:
            sys.print_exception(e)

        line_y = 0
        net_config = sta_if.ifconfig()
        try:
            display.draw_text8x8(0, 8, 'Network config:', WHITE)
        except Exception as e:
            sys.print_exception(e)
        print('Network config:', net_config)

        for i in net_config:
            line_y += 8
            time.sleep(1)
            try:
                display.draw_text8x8(0, line_y, i, WHITE)
            except Exception as e:
                sys.print_exception(e)
        time.sleep(1)
        first_time_conn = 0
        try:
            display.clear()
        except Exception as e:
            sys.print_exception(e)
    return first_time_conn

def create_access_point(ssid, password):
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)
    ap_if.config(essid=ssid, password=password)
    
            

def show_mac():
    mac_address = sta_if.config('mac')
    
    mac_address = binascii.hexlify(mac_address, ':').decode()
    return str(mac_address)

def show_hotspot_ip():
    ap_if = network.WLAN(network.AP_IF)
    
    sta_if.active(False)
    if ap_if.active():
        return ap_if.ifconfig()[0]
    else:
        return None

def show_ip():
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        return sta_if.ifconfig()[0]
    else:
        return None
    