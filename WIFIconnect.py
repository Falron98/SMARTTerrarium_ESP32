import network

def connect_to_network():
    network.WLAN(network.AP_IF).active(False)
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect("Redmi", "12345678")
        while not sta_if.isconnected():
            pass

    print('Network config:', sta_if.ifconfig())
