#!/usr/bin/python3
from sense_hat import SenseHat
from time import sleep, strftime

# Controls

# Function that will be called when the joystick is middle clicked
# Switches between date and time
def change(event):
    if event.action == 'pressed' and event.direction == 'middle':
        global switch
        switch = not switch

# This function will rotate the text
def rotate(event):
    if event.action == 'pressed':
        match event.direction:
            case 'up':
                sense.set_rotation(180)
            case 'left':
                sense.set_rotation(90)
            case 'right':
                sense.set_rotation(270)
            case 'down':
                sense.set_rotation(0)


if __name__ == "__main__":
    # Initialise the Sense Hat
    sense = SenseHat()
    sense.clear()
    switch = False
    
    while True:
        # Takes current time and date
        # Converts each number into integer
        # Converts again into a binary string
        # Then splits the number into a list of bits

        # Splitter
        border = '00000000'

        # Date values
        day    = format(int(strftime("%w")), '08b')
        date   = format(int(strftime("%d")), '08b')
        month  = format(int(strftime("%m")), '08b')

        #Time values
        hour   = format(int(strftime("%H")), '08b')
        minute = format(int(strftime("%M")), '08b')
        second = format(int(strftime("%S")), '08b')


        # The input list
        sense.stick.direction_middle = change
        # Inputting a direction on the joystick will call the function to rotate the text
        sense.stick.direction_up     = rotate
        sense.stick.direction_down   = rotate
        sense.stick.direction_left   = rotate
        sense.stick.direction_right  = rotate

        #Toggles boolean when button pressed
        # User can change display from time to date by clicking the joystick
        if switch == False:
            values = [hour,hour,border,minute,minute,border,second,second]
        else:
            values = [day,day,border,date,date,border,month,month]

        # Output list
        # Output list must be a single list with 64 values
        # This is what will be shown on the led matrix
        matrix = []

        # Color array
        # The colors follow the order of the values recorded
        colors = [[0,100,100],[0,100,100],[0,0,0],[0,0,100],[0,0,100],[0,0,0],[100,0,100],[100,0,100]]

        # Will iterate through each value and append it to the output list
        # Collapses 8x8 array into 1x64 array, which is needed for set_pixels()
        # The y axis will pull the color value from the array to color code the rows
        for y in range(len(values)):
            for x in range(len(values[y])):
                if values[y][x] == '0':
                    matrix.append([0,0,0])
                
                elif values[y][x] == '1':
                    matrix.append(colors[y])
        
        sense.clear()
        sense.set_pixels(matrix)
        sleep(0.1)
