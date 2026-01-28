from gpiozero import RGBLED, Button
from time import sleep
from random import uniform
from colorzero import Color

led = RGBLED(26,19,13)
l_btn = Button(21)
r_btn = Button(20)
count = 0

def start():
    print("Get ready...")

    for i in range(3):
        led.color = Color(255,0,0)
        sleep(0.5)
        led.off()
        sleep(0.5)

    sleep(uniform(5,10))
    led.color = Color(0,0,255)

start()
while True:
    count+= 1
    sleep(0.001)

    if l_btn.is_active == True or r_btn.is_active == True:
        print("Left!") if l_btn.is_active == True else print("Right!")
        led.color = Color(0,255,0)
        print("You took " + str(count) + "ms.")
        print("Do you want to continue? Press left to stop. Press right to continue.")
        sleep(1)
        while True:
            if l_btn.is_active == True:
                print("Stopping game!")
                quit()
            elif r_btn.is_active == True:
                print("Restarting game!")
                count = 0
                start()
                break
