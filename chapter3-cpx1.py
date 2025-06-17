# Joe Melia EET-107

from adafruit_circuitplayground import cp
import time

while True:
    if cp.switch: 
        cp.red_led = True
    else:
        cp.red_led = False
    

