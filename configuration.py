from mySetup import display, WHITE
from WIFIconnect import show_hotspot_ip, create_access_point
import time


def first_config():
    try:
        display.draw_text8x8(0, 8, "Connect to hotspot with:", WHITE)
        display.draw_text8x8(0, 16, "SSID: ESP32", WHITE)
        display.draw_text8x8(0, 24, "Password: 123", WHITE)
    except Exception as e:
        print(e)
        
    time.sleep(5)
    create_access_point("ESP32","123")
    time.sleep(5)
    hotspot_ip = str(show_hotspot_ip())
    try:
        display.draw_text8x8(0, 40, "Connect to FTP server and send files", WHITE)
        display.draw_text8x8(0, 48, hotspot_ip+":21", WHITE)
        display.draw_text8x8(0, 72, "Next, restart board", WHITE)
    except Exception as e:
        print(e)