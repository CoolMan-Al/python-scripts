from random import randint
from sense_hat import SenseHat
from time import sleep

def roll():
    sense.show_message(str(randint(0,20)), text_colour=[randint(0,100),randint(0,100),randint(0,100)])
    sense.clear()
    sleep(3)

sense = SenseHat()
sense.clear()

pix = [randint(0,100),randint(0,100),randint(0,100)]

sense.stick.direction_any = roll

while True:
    gyro = sense.get_accelerometer_raw()
    for i in gyro:
        gyro[i] = round(gyro[i])
    
    if gyro['x'] != 0 or gyro['y'] != 0 or gyro['z'] != 1:
        roll()
