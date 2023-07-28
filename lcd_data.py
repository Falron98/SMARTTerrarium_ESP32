from mySetup import display, unispace
from ili9341 import color565
from sensor import read_sensor, sensors_values
from collections import deque
from buttons_mapping import button_listener
from connection import send_sensor_data
from config_file import *
import time
import uasyncio as asyncio

LCD_WIDTH = int(LCD_values["LCD_WIDTH"])
LCD_HEIGHT = int(LCD_values["LCD_HEIGHT"])

graph_x = int(round(LCD_WIDTH/20)) # 16
graph_y = int(round(LCD_HEIGHT/16)) # 15
graph_width = int(round(LCD_WIDTH/1.1)) # 291
graph_height = int(round(LCD_HEIGHT/1.2)) # 200
graph_x_width = graph_x + graph_width  # 307
graph_y_height = graph_y + graph_height # 215
text_size = 8

min_value = 20
max_value = 40

sensors_dict_data = {}
mode = 1
sensor_mode = "temperature"

key = -1
key_first = 0
key_second = 0



async def show_sensor_data():
    
    global sensors_values, key_first, key_second
    
    button = await button_listener()
    
    keys = list(sensors_dict_data.keys())
    
    if len(keys) > 1:
        while True:
            if key_first != key_second:
                break
            else:
                key_second += 1
                if key_second >= len(keys):
                    key_second = 0
    if button == 0:
        button = 2
    elif button == 6:
        button = 0

    
    if button == 1:
        key_first += 1
        if key_first >= len(keys):
            key_first = 0
                
        if len(keys) > 1:
            while True:
                key_second += 1
                if key_second >= len(keys):
                    key_second = 0
                if key_first != key_second:
                    break
        display.clear()
        button = 2
    
    display.fill_rectangle(round((LCD_WIDTH/20)+(4*text_size)), round(LCD_HEIGHT/8), 3*text_size, round(LCD_HEIGHT-(LCD_HEIGHT/8)-(LCD_HEIGHT/10)), color565(0,0,0))
    display.fill_rectangle(round(LCD_WIDTH - (LCD_WIDTH/4)+(2.5*text_size)), round(LCD_HEIGHT/8), 3*text_size, round(LCD_HEIGHT-(LCD_HEIGHT/8)-(LCD_HEIGHT/10)), color565(0,0,0))
        
    if len(keys) > 0:
        first_value = int(sensors_values[keys[key_first]]['value'])
    else:
        first_value = None
   
    if len(keys) > 1:
        second_value = int(sensors_values[keys[key_second]]['value'])
    else:
        second_value = None
    
    try:
        if first_value is not None:
            display.draw_text8x8(round(LCD_WIDTH/20), round(LCD_HEIGHT-(LCD_HEIGHT/10)), sensors_values[keys[key_first]]['category'], color565(255, 128, 0))
            display.fill_rectangle(round((LCD_WIDTH/20)+(4*text_size)), round(LCD_HEIGHT-(LCD_HEIGHT/8)-first_value), 3*text_size, first_value, color565(255,255,255))
            display.draw_text8x8(round((LCD_WIDTH/20)+(4.5*text_size)), int(LCD_HEIGHT-(LCD_HEIGHT/10) + (1.5*text_size)), str(keys[key_first])[0], color565(0, 0, 0), background=color565(255,255,255))
        display.draw_text8x8(round((LCD_WIDTH/20)+(4.5*text_size)), round(LCD_HEIGHT-(LCD_HEIGHT/8)-(2*text_size)), str(first_value), color565(0, 0, 0), background=color565(255,255,255))
        if second_value is not None:
            display.draw_text8x8(round(LCD_WIDTH - (LCD_WIDTH/4) - len(sensors_values[keys[key_second]]['category'])), round(LCD_HEIGHT-(LCD_HEIGHT/10)), sensors_values[keys[key_second]]['category'], color565(255, 128, 0))
            display.draw_text8x8(round(LCD_WIDTH - (LCD_WIDTH/4)+(3*text_size)), round(LCD_HEIGHT-(LCD_HEIGHT/10) + int(1.5*text_size)), str(keys[key_second])[0], color565(0, 0, 0), background=color565(255,255,255))
            display.fill_rectangle(round(LCD_WIDTH - (LCD_WIDTH/4)+(2.5*text_size)), round(LCD_HEIGHT-(LCD_HEIGHT/8)-second_value), 3*text_size, second_value, color565(255,255,255))
        display.draw_text8x8(round(LCD_WIDTH - (LCD_WIDTH/4)+(3*text_size)), round(LCD_HEIGHT-(LCD_HEIGHT/8)-(2*text_size)), str(second_value), color565(0, 0, 0), background=color565(255,255,255))
    except Exception as e:
        print(e)
        
    
    if button != 2:
        try:
            display.clear()
        except Exception as e:
            print(e)
        
    return button

        
def draw_graph(sensor_mode):
    
    display.draw_rectangle(graph_x, graph_y, graph_width, graph_height, color565(255,255,255))
    j = min_value
    
    for x in range (graph_y, graph_height+1, round(graph_height/2)):

        display.draw_line(graph_x, x, graph_x+2, x, color565(255,255,255))
        display.draw_text8x8(0,(graph_y_height+graph_y-4)-x, str(j), color565(255,255,255))
        j += int((max_value-min_value)/2)
    display.draw_text8x8(0, graph_y-8, str(max_value), color565(255,255,255))
    display.draw_text8x8(3*text_size, graph_y-8, str(sensor_mode), color565(255, 128, 0))

async def draw_data(array):
    display.fill_rectangle(graph_x, graph_y_height, graph_width, LCD_HEIGHT - graph_y_height, color565(0,0,0))
    display.fill_rectangle(graph_x+3,graph_y+1,graph_width-4, graph_height-2,color565(0,0,0))
    for x in range(len(array)):
        display.fill_rectangle(int((graph_width/9)+(x*((graph_width/9)+(graph_width/27)))),
                               int(graph_y_height-((((array[x] if array[x] >= min_value and array[x] < max_value else(min_value if array[x] < min_value else max_value)) - min_value)/(max_value-min_value))*graph_height)),
                               int(graph_width/9),
                               int(((array[x] if array[x] > min_value and array[x] < max_value else (min_value if array[x] < min_value else max_value)) - min_value)/(max_value-min_value)*graph_height),
                               color565(255,255,255))
        display.draw_text8x8(int((round(graph_width/9))+(x*((graph_width/9)+(graph_width/27)))+graph_x-text_size), graph_y_height +(text_size), str(array[x]), color565(255,255,255))


async def draw_data_lines(array):
    display.fill_rectangle(graph_x, graph_y_height, graph_width, LCD_HEIGHT - graph_y_height, color565(0,0,0))
    display.fill_rectangle(graph_x+3,graph_y_height+text_size,graph_width-4, LCD_HEIGHT - graph_y_height - text_size,color565(0,0,0))
    display.fill_rectangle(graph_x+3,graph_y+1,graph_width-4, graph_height-2,color565(0,0,0))
    for x in range(len(array)):
        if x < 1:
            display.fill_circle((30)+(x*45), int(round(graph_y_height-((((array[x] if array[x] > min_value and array[x] < max_value else (min_value if array[x] < min_value else max_value)) - min_value)/(max_value-min_value))*graph_height))), round(text_size/2), color565(255,255,255))
            display.draw_text8x8(((30)+(x*45))-(text_size if array[x] > 9 else int(text_size/2)), int(round(graph_y_height-((((array[x] if array[x] > min_value and array[x] < max_value else (min_value if array[x] < min_value else max_value)) - min_value)/(max_value-min_value))*graph_height)))+(text_size), str(array[x]), color565(255,255,255))
        if x >= 1:
            display.fill_circle((30)+(x*45), int(round(graph_y_height-((((array[x] if array[x] > min_value and array[x] < max_value else (min_value if array[x] < min_value else max_value)) - min_value)/(max_value-min_value))*graph_height))), round(text_size/2), color565(255,255,255))
            display.draw_text8x8(((30)+(x*45))-(text_size if array[x] > 9 else int(text_size/2)),
                                 int(round(graph_y_height-((((array[x] if array[x] > min_value and array[x] < max_value else (min_value if array[x] < min_value else max_value)) - min_value)/(max_value-min_value))*graph_height)))+(text_size),
                                 str(array[x]), color565(255,255,255))
            display.draw_line((30)+((x-1)*45), int(round(graph_y_height-((((array[x-1] if array[x-1] > min_value and array[x-1] < max_value else (min_value if array[x-1] < min_value else max_value)) - min_value)/(max_value-min_value))*graph_height))), (30)+(x*45), int(round(graph_y_height-((((array[x] if array[x] > min_value and array[x] < max_value else (min_value if array[x] < min_value else max_value)) - min_value)/(max_value-min_value))*graph_height))), color565(255,255,255))

async def sensors_dict_data_append():
    global sensors_dict_data
    
    for x in sensors_values:
        if sensors_values[x]['category'] == 'humidity' or sensors_values[x]['category'] == 'temperature':
            if x not in sensors_dict_data:
                sensors_dict_data[x] = []
            if len(sensors_dict_data[x]) > 5:
                sensors_dict_data[x] = sensors_dict_data[x][1:] + [sensors_values[x]['value']]
            else:
                sensors_dict_data[x].append(sensors_values[x]['value'])

async def sensor_array():
    
    global sensors_dict_data
    global sensors_values
    global mode
    global sensor_mode
    global min_value, max_value
    global key
    
    button = await button_listener()
    
    keys = list(sensors_dict_data.keys())
    if len(keys) > 0:
        while True:
            picked_key = sensors_dict_data[keys[key]]
            if sensors_values[keys[key]]['category'] == 'humidity' or sensors_values[keys[key]]['category'] == 'temperature':
                break
            else:
                key += 1
                if key >= len(keys):
                    key = 0

    if button == 0:
        button = 3
    elif button == 2:
        try:
            display.clear()
        except Exception as e:
            print (e)
        
        if len(keys) > 0:
            while True:
                key += 1
                if key >= len(keys):
                    key = 0
                picked_key = sensors_dict_data[keys[key]]
                if sensors_values[keys[key]]['category'] == 'humidity' or sensors_values[keys[key]]['category'] == 'temperature':
                    break
        button = 3
            
    elif button == 1:
        if mode < 2:
            mode += 1
        else:
            mode = 1
        try:
            display.fill_rectangle(graph_x, graph_y_height, graph_width, LCD_HEIGHT - graph_y_height, color565(0,0,0))
        except Exception as e:
            print (e)
        button = 3
    else:
        button = 0
    if len(keys) > 0:
        min_value = sensors_values[keys[key]]['min_val']
        max_value = sensors_values[keys[key]]['max_val']
        sensor_mode = sensors_values[keys[key]]['category']
        data_array = picked_key
    else:
        min_value = 0
        max_value = 100
        sensor_mode = None
        data_array = [0,0,0,0,0,0]
        
    draw_graph(sensor_mode)
    
    if mode == 1:
        await draw_data(data_array)
    elif mode == 2:
        await draw_data_lines(data_array)
    
    if button != 3:
        try:
            display.clear()
        except Exception as e:
            print ("No LCD found {}".format(e))

    return button
