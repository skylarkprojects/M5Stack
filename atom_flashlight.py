from m5stack import *
from m5ui import *
from uiflow import *
import time
import machine, neopixel

def change_rgb(colour, np):
  
  if colour == 'red':
    np[0] = (64, 0, 0) # set to red, full brightness
    np.write()
    
  elif colour == 'green':
    np[0] = (0, 64, 0) # set to green, half brightness
    np.write()
    
  elif colour == 'blue':
    np[0] = (0, 0, 64)  # set to blue, quarter brightness
    np.write()
    
  else:
    np[0] = (0, 0, 0)
    np.write()

def flashlights(np):

  colours = {
        0 : 'red',
        1 : 'blue'
            }  
            
  x = 1
  
  while True:
    
    time.sleep(1)
    change_rgb(colours[0],np)
    time.sleep(1)
    change_rgb(colours[1],np)    
    
    x = x + 1
    
    if x >= 10:
      break
    


pin = machine.Pin(27)
bits = 1

np = neopixel.NeoPixel(pin, bits)

flashlights(np)

