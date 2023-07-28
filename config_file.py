import ujson

def save_config_file(filename, obj_write):
    
    try:
        json_object = ujson.dumps(obj_write)
    
        with open(filename, "w") as outfile:
            outfile.write(json_object)
            
    except Exception as e:
        
        print(e)

def open_config_file(filename):
    
    try:
        with open(filename, 'r') as openfile:
            # Reading from json file
            json_object = ujson.load(openfile)
        return json_object
    
    except Exception as e:
        print(e)

def load_ftp_files():
    try:
        conf_file = open_config_file("config.json")
        ftp_file = open_config_file("ftp_config_file.json")
        print("Loading data from FTP")
        FTP_TCP_values = ftp_file["TCP"]
        FTP_MQTT_values = ftp_file["MQTT"]
        FTP_WIFI_values = ftp_file["WIFI"]

        conf_file["TCP"]["TCP_SERVER_IP"] = FTP_TCP_values["TCP_SERVER_IP"]
        conf_file["TCP"]["TCP_PORT"] = FTP_TCP_values["TCP_PORT"]
        conf_file["MQTT"]["MQTT_SERVER_IP"] = FTP_MQTT_values["MQTT_SERVER_IP"]
        conf_file["MQTT"]["MQTT_PORT"] = FTP_MQTT_values["MQTT_PORT"]
        conf_file["WIFI"]["WIFI_SSID"] = FTP_WIFI_values["WIFI_SSID"]
        conf_file["WIFI"]["WIFI_PASSWORD"] = FTP_WIFI_values["WIFI_PASSWORD"]
        print("Writing to config")
        save_config_file("config.json", conf_file)
    except Exception as e:
        print(e)

config_values = open_config_file("config.json")
sensor_config_values = open_config_file("sensors_config.json")
MQTT_values = config_values["MQTT"]
TCP_values = config_values["TCP"]
WIFI_values = config_values["WIFI"]
LCD_values = config_values["LCD"]
BUTTONS_values = config_values["BUTTONS"]
PWM_values = config_values["PWM"]
SENSORS = sensor_config_values["SENSORS"]