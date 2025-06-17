#Joe Melia EET-107

from adafruit_circuitplayground import cp
import time

while True:
    if cp.button_a:
        cp.play_file("bloop_x.wav")
    if cp.button_b:
        cp.play_file("blip.wav")
