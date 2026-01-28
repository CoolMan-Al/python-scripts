from gpiozero import Button
from signal import pause

switch = Button(4)

switch.when_pressed = print("BUTTONED")

pause()