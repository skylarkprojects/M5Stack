
# a simple atom lite function to create a flashing light out of the 'G27' pin
# works in Thonny, and in https://flow.m5stack.com/#video

# uses
#import machine, neopixel
#np = neopixel.NeoPixel(machine.Pin(27), 1)
#np[0] = (0, 0, 64)  # set to blue
#np.write()

# refer docs:
# https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html


import time
import machine, neopixel



class flashlights:
  
  
  def __init__(self,pin_number,pixels):
    self.pin_number = pin_number
    self.pixels = pixels
    self.np = neopixel.NeoPixel(pin_number, pixels)
    
    
  def change_rgb(self, colour):
    
    if colour == 'red':
      self.np[0] = (64, 0, 0) # set to red, quarter brightness
      self.np.write()
      
    elif colour == 'green':
      self.np[0] = (0, 64, 0) # set to green, quarter brightness
      self.np.write()
      
    elif colour == 'blue':
      self.np[0] = (0, 0, 64)  # set to blue, quarter brightness
      self.np.write()
      
    else:
      self.np[0] = (0, 0, 0)
      self.np.write()

  def police_lights(self):
  
    colours = {
          0 : 'red',
          1 : 'blue'
              }  
              
    x = 1
    
    while True:
      
      time.sleep(1)
      self.change_rgb(colours[0])
      time.sleep(1)
      self.change_rgb(colours[1])    
      
      x = x + 1
      
      if x >= 10:
        break
    

def main():
  
  pin_number = machine.Pin(27)
  pixels = 1
  
  flasher = flashlights(pin_number, pixels)
  
  flasher.police_lights()
  

main()
  
  
