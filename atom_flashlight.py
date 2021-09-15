import machine
import neopixel
import time

gpio = 27
no_pixels = 1

pin = machine.Pin(gpio)
x = 0

while True
        
    np[0] = (255, 0 , 0)

    time.sleep(1)
    np[0] = (0, 255 , 0)

    time.sleep(1)
    np[0] = (0, 0 , 255)
    
    time.sleep(1)
     x = x + 1
     
     if x == 20:
         break
        
    
