#!/usr/bin/python3
from rgbmatrix5x5 import RGBMatrix5x5
from time import sleep

#How to use the 5x5 LED matrix 

#Initialise the matrix
matrix = RGBMatrix5x5()

#Turns off all pixels after script finishes
matrix.set_clear_on_exit()

matrix.set_brightness(0.2)

#Fill all pixels
matrix.set_all(255,255,255)

#Needed to actually display pixels
matrix.show()

sleep(1)

matrix.clear()

#Set individual pixels
matrix.set_pixel(0,0,255,255,255)
matrix.set_pixel(4,4,255,0,0)
matrix.set_pixel(0,4,0,255,0)
matrix.set_pixel(4,0,0,0,255)

matrix.show()

sleep(1)

matrix.clear()

#Set multiple pixels using index
#First row of pixels is [0,5, 10, 15, 20]
#Use range to iterate through matrix

for i in range(2):
    matrix.set_multiple_pixels(range(1,25,2), (255,0,0), (255,255,0))
    matrix.show()
    sleep(0.5)
    matrix.clear() 

    matrix.set_multiple_pixels(range(0,25,2),(0,255,0),(0,255,255))
    matrix.show()
    sleep(0.5)
    matrix.clear()

    matrix.set_multiple_pixels(range(1,25,2),(0,0,255),(255,0,255))
    matrix.show()
    sleep(0.5)
    matrix.clear()
    
    matrix.set_multiple_pixels(range(0,25,2), (255,255,255))
    matrix.show()
    sleep(0.5)
    matrix.clear()

for i in range(2):
    #Letter T
    matrix.set_multiple_pixels(range(0, 25, 5), (255,0,0))
    matrix.set_multiple_pixels(range(11,15), (255,0,0))
    matrix.show()
    sleep(0.5)
    matrix.clear()

    #Letter E
    matrix.set_multiple_pixels(range(5,16,5),(0,255,0))
    matrix.set_multiple_pixels(range(7,18,5),(0,255,0))
    matrix.set_multiple_pixels(range(9,20,5),(0,255,0))
    matrix.set_multiple_pixels(range(6,10,2),(0,255,0))
    matrix.show()
    sleep(0.5)
    matrix.clear()

    #Letter S
    matrix.set_multiple_pixels(range(5,16,5),(0,0,255))
    matrix.set_multiple_pixels(range(7,18,5),(0,0,255))
    matrix.set_multiple_pixels(range(9,20,5),(0,0,255))
    matrix.set_multiple_pixels(range(6,19,12),(0,0,255))
    matrix.show()
    sleep(0.5)
    matrix.clear()

    #Letter T
    matrix.set_multiple_pixels(range(0, 25, 5), (255,255,255))
    matrix.set_multiple_pixels(range(11,15), (255,255,255))
    matrix.show()
    sleep(0.5)
    matrix.clear()
