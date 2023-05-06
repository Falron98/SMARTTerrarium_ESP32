import ujson

def save_config_file():
    
    try:
        json_object = ujson.dumps(dict)
    
        with open("config.json", "w") as outfile:
            outfile.write(json_object)
            
    except Exception as e:
        
        print(e)

def open_config_file():
    
    try:
        with open("config.json", 'r') as openfile:
            # Reading from json file
            json_object = ujson.load(openfile)
        return json_object
    
    except Exception as e:
        print(e)

values = open_config_file()

MQTT_ID_NAME = values["MQTT_ID_NAME"]
MQTT_PORT = int(values["MQTT_PORT"])
MQTT_SERVER_IP = values["MQTT_SERVER_IP"]

WIFI_SSID = values["WIFI_SSID"]
WIFI_PASSWORD = values["WIFI_PASSWORD"]
ESP_MAC_ADDRESS = values["ESP_MAC_ADDRESS"]
        
LCD_WIDTH = int(values["LCD_WIDTH"])
LCD_HEIGHT = int(values["LCD_HEIGHT"])
LCD_ROTATION = int(values["LCD_ROTATION"])

TFT_CLK_PIN = int(values["LCD_CLK_PIN"])
TFT_MOSI_PIN = int(values["LCD_MOSI_PIN"])
TFT_MISO_PIN = int(values["LCD_MISO_PIN"])

TFT_CS_PIN = int(values["LCD_CS_PIN"])
TFT_RST_PIN = int(values["LCD_RST_PIN"])
TFT_DC_PIN = int(values["LCD_DC_PIN"])

FONT_DIR = values["FONT_DIR"]
FONT_WIDTH = int(values["FONT_WIDTH"])
FONT_HEIGHT = int(values["FONT_HEIGHT"])

BUTTON_ADC_PIN = int(values["BUTTON_ADC_PIN"])

HUMIDITY_SENSOR_PIN = int(values["HUMIDITY_SENSOR_PIN"])
