import neopixel
import machine


class led_indicator:

    def __init__(self, led_pin_number):
        self.led_pin = led_pin_number

    def set_light_success(self):
        # if connection is successful, set light to green
        np = neopixel.NeoPixel(machine.Pin(led_pin_number),1)
        np[0] = (0, 128, 0)
        np.write()

    def set_light_fail():
        # if connection is successful, set light to red
        np = neopixel.NeoPixel(machine.Pin(led_pin_number),1)
        np[0] = (128, 0, 0)
        np.write()

    def set_light_connected():
        # if connection is successful, set light to blue
        np = neopixel.NeoPixel(machine.Pin(led_pin_number),1)
        np[0] = (0, 0, 128)
        np.write()
