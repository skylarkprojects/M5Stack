
import network
import machine
from wifi import ensure_webrepl
from wifi import about
from wifi import keys
from wifi import led_connection_indicator as light_indicator

class create:

    def __init__(self,):
        # initiate session variables
        """ nothing to initiate"""

    def connection(wifi, pwd):
        ## function creates a connection between the ESP32 and your desired local WiFi network
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect(self.wifi, self.wifi_pwd)
            while not sta_if.isconnected():
                pass
        print('network config:', about.connection.GetInfo())


def connect():
    # a function to initiate the above classes and create a new connection
    # optional features to set LED pixel to:
    # blue to denote connection success
    # red to denote connection fail
    # assumes led is single pixel (i.e. my M5Stack has GPIO pin 27 on top which is a single light a.k.a. pixel)

    try:
        ensure_webrepl.connectToWebrepl()
        w = create.connection(keys.get_creds['wifi_name'], keys.get_creds['wifi_password'])

        # (OPTIONAL CODE BELOW) sets my M5Stack Atom G27 Pin to blue to denote a successful conneciton
        #led.set_light_connected(27)

        print('connection successful')

    except Exception as e:
        # (OPTIONAL CODE BELOW) sets my M5Stack Atom G27 Pin to red to denote a successful conneciton
        #led.set_light_connected(27)
        print('connection failed')

# enabler below if you want to test this script in silo by running this script
#connect()
