from mySetup import display, unispace, LCD_WIDTH, LCD_HEIGHT
from ili9341 import color565
from sensor import read_sensor
from collections import deque
from buttons_mapping import button_listener
from connection import send_sensor_data
from config_file import *
import time
import uasyncio as asyncio

graph_x = int(round(LCD_WIDTH/20))
graph_y = int(round(LCD_HEIGHT/16))
graph_width = int(round(LCD_WIDTH/1.1))
graph_height = int(round(LCD_HEIGHT/1.2))
graph_x_width = graph_x + graph_width
graph_y_height = graph_y + graph_height

async def show_sensor_data():
    running = True
    while running:
        values = await asyncio.gather(button_listener(), read_sensor())
        data = values[1]
        await send_sensor_data(data)
        print("data {}".format(data))
        try:
            display.draw_text(round(LCD_WIDTH/2), round(LCD_HEIGHT/2), str(data), unispace, color565(255, 128, 0))
        except Exception as e:
            print ("No LCD found {}".format(e))
        if values[0] != 0:
            running = False
        await asyncio.sleep(1)


#show_sensor_data()
time.sleep(1)
try:
    #display.clear()
    pass
except Exception as e:
    print("No LCD found")
        
def draw_graph():
    
    display.draw_rectangle(graph_x, graph_y, graph_width, graph_height, color565(255,255,255))
    j = 0
    
    for x in range (graph_y, graph_height+1, round(graph_height/4)):
        print(x)

        display.draw_line(graph_x, x, graph_x+2, x, color565(255,255,255))
        display.draw_text8x8(0,(graph_y_height+graph_y-4)-x, str(j), color565(255,255,255))
        j += 25
    display.draw_text8x8(0, graph_y-8, str(100), color565(255,255,255))

async def draw_data(array):
    display.fill_rectangle(graph_x+3,graph_y+1,graph_width-4, graph_height-2,color565(0,0,0))
    for x in range(len(array)):
        display.fill_rectangle(int((round(graph_width/9))+(x*((graph_width/9)+(graph_width/27)))),
                               int(round(graph_y_height-((array[x]*graph_height)/100))),
                               int(round(graph_width/9)),
                               int(round((array[x]*graph_height)/100)),
                               color565(255,255,255))

def draw_data_lines():
    array = sensor_array()
    display.fill_rectangle(18,16,286,198,color565(0,0,0))
    for j in range (0, 216, 50):
        display.draw_line(15,14+j,17,14+j, color565(255,255,255))
        display.draw_text8x8(0,(214-4)-j,str(round(j/2)), color565(255,255,255))
    for x in range(len(array)):
        if x < 1:
            display.fill_circle((30)+(x*45), 215-array[x], 4, color565(255,255,255))
            display.draw_text8x8(((30)+(x*45))-8, 215-array[x]+12, str(array[x]), color565(255,255,255))
        if x >= 1:
            display.fill_circle((30)+(x*45), 215-array[x], 4, color565(255,255,255))
            display.draw_text8x8(((30)+(x*45))-8, 215-array[x]+12, str(array[x]), color565(255,255,255))
            display.draw_line((30)+((x-1)*45), 215-array[x-1], (30)+(x*45), 215-array[x], color565(255,255,255))
    

async def sensor_array():
    
    data_array = []
    draw_graph()
    running = True
    while running:
        values = await asyncio.gather(button_listener(), read_sensor())
        sensor_data = values[1]
        await send_sensor_data(sensor_data)
        if len(data_array) > 5:
            data_array = data_array[1:] + [sensor_data]
        else:
            data_array.append(sensor_data)
        await draw_data(data_array)
        if values[0] != 0:
            running = False
        await asyncio.sleep(1)
    try:
        display.clear()
    except Exception as e:
        print ("No LCD found {}".format(e))
