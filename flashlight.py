# Using a Pin with micropython
# Make sure you have the LED checkbox marked!

import machine

import time

print('starting light')


class switch:
    
    def __init__(self, pin):
        
        self.pin = pin
        
        
    def flashlight(self):
        
        print('flashlight(self)')
        
        x = 0
        boolean = 0
        while True:
            
            if x > 11:
                break
            else:
                
                if boolean == 1:
                    boolean = 0
                else:
                    boolean = 1
                
                self.pin(boolean)
                
                time.sleep(1)
                print('1 second')
                x = x + 1
                         
y12 = machine.Pin('Y12')          
m = switch(y12)
                
            
m.flashlight()


