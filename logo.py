from ili9341 import color565
from mySetup import display, unispace
from WIFIconnect import show_mac
import time

def start_logo():
    try:
        display.clear()
        display.draw_image("python.raw", 96, 56, 128, 128)
        time.sleep(2)
        display.draw_text(70, 200, 'SMART Terrarium', unispace, color565(255, 255, 255))
        time.sleep(5)
        display.clear()
    except Exception as e:
        print("No LCD found")

def mac_image():
    try:
        display.clear()
        mac = show_mac()
        display.draw_text(0, 128, str(mac), unispace, color565(255, 255, 255))
        time.sleep(5)
        display.clear()
    except Exception as e:
        print("No LCD found {}".format(e))
        
        
def qr_code():
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    mac = show_mac()
    qr.add_data(str(mac))
    qr.make(fit=True)

    # save the QR code as a raw file
    with open('qrcode.raw', 'wb') as f:
        f.write(qr.get_matrix().tobytes())
