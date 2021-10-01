# wifi-micropython

#### About

##### This package is a lite package for micropython to enable an ESP32 to connect to your local wifi network

## Installation

1) Copy the entire 'wifi' file into your micropython main directory

![image](https://user-images.githubusercontent.com/87293579/135570354-f6844b79-c8bf-41bc-8260-58e601badf4a.png)


2) Update wifi/keys.py by inserting your wifi name and wifi password into the dispatch table between the "quote marks"


3) Insert the following code into your 'boot.py' file in the main directory

# --- START OF boot.py CODE ---
# This file is executed on every boot (including wake-boot from deepsleep)

from wifi import wifi

def device_boot():
    try:
        wifi.connect()
        print('wifi process executed')
        
        
    except Exception as e:
        
        print('boot.py failed')
        print(e)


device_boot()
# --- END OF boot.py CODE ---
# at the conclusion of device_boot(), the boot will run main()




##### Don't forget to jump onto your wifi router and reserve the local IP so the address doesn't change every time you want to access it ;-)
