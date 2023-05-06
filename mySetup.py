from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from config_file import *


unispace = XglcdFont(FONT_DIR, FONT_WIDTH, FONT_HEIGHT)


def create_LCD_SPI():
    try:
        spi = SPI(1, baudrate=40000000, sck=Pin(TFT_CLK_PIN), mosi=Pin(TFT_MOSI_PIN))
        display = Display(spi, dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN), rotation=LCD_ROTATION)
        return display
    except Exception as e:
        return e


def test():
    """Test code."""
    # Baud rate of 40000000 seems about the max
    display = create_LCD_SPI()

    print('Loading fonts...')
    print('Loading unispace')
    print('Fonts loaded.')

    display.draw_text(0, 190, 'Test', unispace,
                      color565(255, 128, 0))

    sleep(9)
    display.clear()
    display.draw_text(190, 239, 'Test', unispace,
                      color565(255, 128, 0),
                      landscape=True)

    sleep(9)
    display.clear()

    display.draw_text(0, 190, 'Test', unispace, color565(255, 128, 0),
                      background=color565(0, 128, 255))

    sleep(9)
    display.cleanup()

display = create_LCD_SPI()
#display = "wot"