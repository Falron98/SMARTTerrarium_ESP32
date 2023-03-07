"""ILI9341 demo (fonts)."""
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont

TFT_CLK_PIN = const(15)
TFT_MOSI_PIN = const(9)
TFT_MISO_PIN = const(8)

TFT_CS_PIN = const(11)
TFT_RST_PIN = const(16)
TFT_DC_PIN = const(13)

def test():
    """Test code."""
    # Baud rate of 40000000 seems about the max
    spi = SPI(1, baudrate=40000000, sck=Pin(TFT_CLK_PIN), mosi=Pin(TFT_MOSI_PIN))
    display = Display(spi, dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN))

    print('Loading fonts...')
    print('Loading unispace')
    unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)
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


test()