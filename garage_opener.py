# Using a Pin with micropython
# Make sure you have the LED checkbox marked!
#https://micropython.org/unicorn/

import machine

import time

class switch:
    
    def __init__(self, pin):
        
        self.pin = pin
                
    def garage_opener(self):
        
        print('Opening garage door!')
        print('  Turning switch on')
        self.pin(1)
        
        time.sleep(3)
        
        print('  Turning switch off')
        self.pin(0)
        
        
y12 = machine.Pin('Y12')          
m = switch(y12)
                
m.garage_opener()



