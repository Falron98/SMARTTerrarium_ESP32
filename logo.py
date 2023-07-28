from ili9341 import color565
from mySetup import display, unispace
import time, sys

def start_logo():
    try:
        display.clear()
        display.draw_image("python.raw", 96, 56, 128, 128)
        time.sleep(2)
        display.draw_text(70, 200, 'SMART Terrarium', unispace, color565(255, 255, 255))
        time.sleep(5)
        display.clear()
    except Exception as e:
        sys.print_exception(e)

