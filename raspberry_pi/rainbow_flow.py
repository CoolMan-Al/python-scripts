from gpiozero import RGBLED, Button
from time import sleep
from colorzero import Color

rgb = RGBLED(26,19,13)
l_btn = Button(21)
r_btn = Button(20)

refresh = 1000
red = 255
green = 0
blue = 0

while True:
    
    while green != 255:
        if l_btn.is_active == False and r_btn.is_active == False:
            green += 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while red != 0:
        if l_btn.is_active == False and r_btn.is_active == False:
            red -= 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while blue != 255:
        if l_btn.is_active == False and r_btn.is_active == False:
            blue += 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while green != 0:
        if l_btn.is_active == False and r_btn.is_active == False:
            green -= 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while red != 255:
        if l_btn.is_active == False and r_btn.is_active == False:
            red += 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
    
    while blue != 0:
        if l_btn.is_active == False and r_btn.is_active == False:
            blue -= 1
        rgb.color = Color(red,green,blue)
        sleep(1/refresh)
