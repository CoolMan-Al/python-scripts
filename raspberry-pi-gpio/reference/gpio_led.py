from gpiozero import LED
from signal import pause
from time import sleep

light = LED(4)

while True:
    light.on()
    sleep(0.1)
    light.off()