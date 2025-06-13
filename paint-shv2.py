#!/usr/bin/python3
from sense_hat import SenseHat
from time import sleep

# Middle click function
# Lets the user press to switch color
# When user holds middle click, will turn into eraser

def change(event):
    global color
    if event.action == 'pressed':
        if color == [0,0,0]:
            color = color_set[0]
        else:
            if color_set.index(color) == len(color_set) - 1:
                color = color_set[0]
            else:        
                color = color_set[color_set.index(color) + 1]
    elif event.action == 'held':
        color = [0,0,0]

# Direction Functions
# Will only use pressed to avoid duplicate movements being passed
# User uses the joystick to change the position of the pixel
# Will paint red if the user tries to move out of bounds

def up(event):
    if event.action == 'pressed':
        global row
        global col
        if row == 0:
            sense.set_pixel(col,row,100,0,0)
        
        else:
            row -= 1
            sense.set_pixel(col,row,color)

def down(event):
    if event.action == 'pressed':
        global row
        global col
        if row == 7:
            sense.set_pixel(col,row,100,0,0)
        
        else:
            row += 1
            sense.set_pixel(col,row,color)

def left(event):
    if event.action == 'pressed':
        global row
        global col
        if col == 0:
            sense.set_pixel(col,row,100,0,0)
        
        else:
            col -= 1
            sense.set_pixel(col,row,color)

def right(event):
    if event.action == 'pressed':
        global row
        global col
        if col == 7:
            sense.set_pixel(col,row,100,0,0)
        
        else:
            col += 1
            sense.set_pixel(col,row,color)

if __name__ == "__main__":
    # Initialisation
    sense = SenseHat()
    sense.clear()

    # Coordinates for pixel position
    row = 0
    col = 0

    # List of colours user can switch through
    # Default font is white
    color_set = [
    [100,100,100],
    [100,0,0],
    [0,100,0],
    [0,0,100],
    [100,100,0],
    [100,0,100],
    [0,100,100],
    [100,0,50],
    [100,50,0]
    ]
    color = color_set[0]
    sense.set_pixel(0,0, color)

    # Controls
    sense.stick.direction_up     = up
    sense.stick.direction_down   = down
    sense.stick.direction_left   = left
    sense.stick.direction_right  = right
    sense.stick.direction_middle = change

    # While loop to keep program running
    while True:
        pass

