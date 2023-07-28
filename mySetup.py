from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from config_file import *

WHITE = color565(255, 255, 255)

FONT_DIR = LCD_values["FONT_DIR"]
FONT_WIDTH = int(LCD_values["FONT_WIDTH"])
FONT_HEIGHT = int(LCD_values["FONT_HEIGHT"])

unispace = XglcdFont(FONT_DIR, FONT_WIDTH, FONT_HEIGHT)

TFT_CLK_PIN = int(LCD_values["LCD_CLK_PIN"])
TFT_MOSI_PIN = int(LCD_values["LCD_MOSI_PIN"])
TFT_DC_PIN = int(LCD_values["LCD_DC_PIN"])
TFT_CS_PIN = int(LCD_values["LCD_CS_PIN"])
TFT_RST_PIN = int(LCD_values["LCD_RST_PIN"])
LCD_ROTATION = int(LCD_values["LCD_ROTATION"])

def create_LCD_SPI():
    try:
        spi = SPI(1, baudrate=40000000, sck=Pin(TFT_CLK_PIN), mosi=Pin(TFT_MOSI_PIN))
        display = Display(spi, dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN), rotation=LCD_ROTATION)
        return display
    except Exception as e:
        return e


display = create_LCD_SPI()