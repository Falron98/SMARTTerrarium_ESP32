# SMARTTerrarium_ESP32
This repository contains the software for the ESP32-based SmartTerrarium project. 
SmartTerrarium is a system designed to monitor and control the environmental conditions in a terrarium for reptiles or other small animals. 
It utilizes an ESP32 microcontroller, various sensors and components to create a smart and automated terrarium.

# Features

Environmental Monitoring: SmartTerrarium can measure temperature, humidity and weight of a bowl of water within the terrarium.

Automatic Control: The system can automatically adjust conditions like lighting to improve environment conditions for the terrarium's inhabitants. It can also automatically refill bowl of water after configuration.

Data Visualization: Data collected from the sensors can be visualized and analyzed on various platforms (including ESP with LCD), allowing users to track environmental trends.

Alerts: SmartTerrarium can send alerts to users when conditions fall outside specified ranges, ensuring the welfare of the animals.

Remote Control: Users can control and monitor the terrarium remotely through a mobile application or web interface. Basic functions can also be controlled on MCU by buttons.

# Prerequisites
- ESP32-S2-KALUGA-1
- DHT22
- FSR-406
- JQC-3ff-S-Z
- Dimmer module
- mini water pump (5V)
  
# Installation
Clone this repository to your local machine:

git clone https://github.com/your-username/smart-terrarium.git

Configure the software by editing the config.py file with your specific settings.

Upload the code to your ESP32 using the MicroPython firmware.

Power on your ESP32 and monitor the logs to ensure it's connected to your network and sensors are functioning correctly.

Access the web interface or mobile app to control and monitor your terrarium (mobile app, web app and server can be found at https://github.com/Smart-Terrarium)

# Examples of connecting components with MCU
## Temperature and humidity sensor
![DHT22](https://github.com/Falron98/SMARTTerrarium_ESP32/assets/61655970/0fef7879-b333-4b9b-b028-c49d61431d3b)
The DHT22 sensor is equipped with three pins: VCC, GND, and DATA. 
To ensure proper operation of the sensor, the following connections have been made between the DHT22 sensor and the ESP32-S2-Kaluga-1 board:

    The VCC of the DHT22 sensor has been connected to the 5V power supply of the microcontroller board.
    The GND of the DHT22 sensor has been connected to the ground of the microcontroller board.
    The OUT of the DHT22 sensor has been connected to a selected GPIO of the microcontroller, which will be responsible for reading data from the sensor.

## Force sensor
![force_sensor](https://github.com/Falron98/SMARTTerrarium_ESP32/assets/61655970/91f3f638-8e5e-4571-9198-61b9b5a2bd04)

In the SmartTerrarium project, the FSR-406 force-sensitive resistor was configured and connected in a way that allows for the measurement of pressure and the weight of the water container. 
To ensure the proper operation of the force-sensitive resistor, a 10 kOhm resistor was used.

The connection between the force-sensitive resistor, the resistor, and the ESP32-S2-Kaluga-1 microcontroller was realized as follows:

    One leg of the force-sensitive resistor was connected to the 5V power supply of the microcontroller board.
    The second leg of the force-sensitive resistor was connected to one end of the 10 kOhm resistor.
    The other end of the 10 kOhm resistor was connected to the ground (GND) of the microcontroller board.
    The midpoint of the connection between the force-sensitive resistor and the resistor was connected to a selected GPIO of the microcontroller, which would be responsible for reading changes in pressure.

## Dimmer module with bulb
![dimmer](https://github.com/Falron98/SMARTTerrarium_ESP32/assets/61655970/c20fadee-63f2-4c04-b440-416122eb9607)

Connection of the dimmer module to the microcontroller:

    The VCC of the dimmer module was connected to the 5V power source of the microcontroller board.
    The GND of the dimmer module was connected to the ground of the microcontroller board.
    The PWM of the dimmer module was connected to one of the GPIO pins of the microcontroller, which would be responsible for controlling the light intensity.

Connection of the dimmer module to the power source and the lamp:

    The AC IN of the dimmer module was connected to the power source, such as an electrical socket.
    The LOAD1 of the dimmer module was connected to the lamp whose light intensity would be regulated.

## Water pump with relay
![water_pump](https://github.com/Falron98/SMARTTerrarium_ESP32/assets/61655970/21d97cca-fb66-43da-8141-d01b4e9fe74f)

Connection of the relay to the mini liquid pump and the adapter:

    The COM terminal of the relay was connected to one of the power inputs of the mini liquid pump.
    The NC terminal of the relay was connected to the 5V power supply of the adapter. In the idle state of the relay (without active control), the connection between COM and NC is closed.
    The ground of the mini liquid pump was connected to the ground of the 5V adapter. This connection is meant to provide a common reference for the circuit.

Connection of the relay to the microcontroller:

    The VCC terminal of the relay was connected to the 5V power supply of the ESP32-S2-Kaluga-1 microcontroller.
    The GND terminal of the relay was connected to the ground of the microcontroller.
    The IN terminal of the relay was connected to one of the microcontroller's pins responsible for controlling the relay.

# Software Usage
    The ESP32-S2-Kaluga-1 microcontroller is equipped with a set of built-in buttons labeled from K1 to K6. These built-in buttons serve as the user interface, allowing direct interaction with the SmartTerrarium system. Each of these buttons has a specific function.

## Main Screen
    On the main screen, various functions can be accessed through the buttons of the ESP32-S2-Kaluga-1 microcontroller:
        Button K5 enables navigation to a chart displaying real-time readings of two sensors, facilitating the monitoring of temperature and humidity in the terrarium.
        Button K4 displays a graph of the latest sensor readings.
        Button K3 provides access to the initial configuration of the board, allowing for the preliminary network setup of the board.
        Button K2 initiates a measurement of the weight of the pressure board. This includes determining the lower and upper weight values that define the range of correct readings. With these values, the microcontroller can accurately monitor changes in the weight of the water container, enabling control of the pump.

## Current Measurements Screen
    On the current measurements screen, you can change which sensors are displayed:
        Button K1: Return to the main screen
        Button K6: Switch to the next pair of displayed sensors.

## Sensor Graph Screen
    The sensor graph screen displays the latest values read from the sensors:
        Button K1: Return to the main screen
        Button K5: Switch to the next sensor on the graph screen
        Button K6: Change the type of chart on the graph screen (bar or point).

## Initial Configuration Screen
    During the initial configuration, instructions regarding the necessary steps are displayed on the LCD screen. At this stage, the microcontroller launches its own access point (hotspot), allowing connection to it.
    Additionally, an FTP server is activated, enabling the transfer of configuration files. To facilitate this process, it is necessary to use the mobile application from the SmartTerrarium project. After successfully uploading the files, a restart of the board is required to apply the settings.

## Pressure Board Configuration Screen
    While on the pressure board sensor configuration screen, in order to set the minimum weight of the water bowl, you place an empty bowl on the board and click button K6. Next, you pour the desired amount of water and click button K5. 
    The data will be saved, and using this data, the microcontroller will control the water level in the bowl.
    
# Acknowledgments
- [micropython-ili9341](https://github.com/rdagger/micropython-ili9341) - Drivers for LCD Screen used in project
- [FTP-Server-for-ESP8266-ESP32-and-PYBD](https://github.com/robert-hh/FTP-Server-for-ESP8266-ESP32-and-PYBD) - Library used for starting FTP server by ESP32 which allows first configuration to start
