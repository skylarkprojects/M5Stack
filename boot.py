
# --- START OF boot.py CODE ---
# example code to insert into your master boot.py file to enable connectivity
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
