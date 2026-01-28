from gpiozero import LED, Button
from time import sleep

light = LED(4)

switch = Button(26)

light.on()

while True:
    if switch.is_active == True:
        if light.is_active == True:
            light.off()
        else:
            light.on()
    
    sleep(0.25)
