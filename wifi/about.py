import network

class connection:

     ## a class that provides additional information about your wifi connection
    # available features include:
    # GetInfo() returning local device IP of ESP
    # IsConnected() returning 1 if device is connected to wifi

    def get_info():
        # returns info about your wifi connection
        sta_if = network.WLAN(network.STA_IF)
        info = sta_if.ifconfig()
        return info


    def is_connected():
        # checks to see if there is a wifi connection and details
        connection_info = wifi_connection.GetInfo()

        if len(connection_info) > 0:
            is_wifi_connection = 1
        else:
            is_wifi_connection = 0

        return is_wifi_connection


    GetInfo = get_info
    IsConnected = is_connected
