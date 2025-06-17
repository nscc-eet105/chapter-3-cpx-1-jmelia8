#Joe Melia EET-107

from adafruit_circuitplayground import cp
import time

while True:
    if cp.touch_A1:
        cp.pixels[6] = (100, 0, 0)
    else:
        cp.pixels[6] = (0, 0, 0)
