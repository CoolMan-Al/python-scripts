from gpiozero import RGBLED,Button
from time import sleep
from colorzero import Color

rgb = RGBLED(17,27,22)

red = 0
green = 0
blue = 0

while True:
    red = 255
    rgb.color = Color(red,green,blue)
    sleep(0.5)

    green = 255
    rgb.color = Color(red,green,blue)
    sleep(0.5)

    red = 0
    rgb.color = Color(red,green,blue)
    sleep(0.5)

    blue= 255
    rgb.color = Color(red,green,blue)
    sleep(0.5)

    green = 0
    rgb.color = Color(red,green,blue)
    sleep(0.5)

    red = 255
    rgb.color = Color(red,green,blue)
    sleep(0.5)

    green = 255
    rgb.color = Color(red,green,blue)
    sleep(0.5)

    red,green,blue = 0,0,0
    rgb.color = Color(red,green,blue)
    sleep(0.5)