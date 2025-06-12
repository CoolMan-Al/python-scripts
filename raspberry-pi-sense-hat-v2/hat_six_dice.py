from random import randint
from sense_hat import SenseHat
from time import sleep

def roll():
    sense.set_pixels(dice[randint(0,5)])
    sleep(3)
    sense.clear()

sense = SenseHat()
sense.clear()

blk = [0,0,0]
pix = [randint(0,100),randint(0,100),randint(0,100)]

dice = [
    [ # One
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,blk,pix,pix,pix,pix,blk,blk,
    blk,blk,pix,pix,pix,pix,blk,blk,
    blk,blk,pix,pix,pix,pix,blk,blk,
    blk,blk,pix,pix,pix,pix,blk,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    ],
    [ # Two
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,pix,pix,pix,blk,blk,blk,blk,
    blk,pix,pix,pix,blk,blk,blk,blk,
    blk,pix,pix,pix,blk,blk,blk,blk,
    blk,blk,blk,blk,pix,pix,pix,blk,
    blk,blk,blk,blk,pix,pix,pix,blk,
    blk,blk,blk,blk,pix,pix,pix,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    ],
    [ # Three
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,blk,blk,pix,pix,blk,blk,blk,
    blk,blk,blk,pix,pix,blk,blk,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    ],
    [ # Four
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    ],
    [ # Five
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,blk,blk,pix,pix,blk,blk,blk,
    blk,blk,blk,pix,pix,blk,blk,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    ],
    [ # Six
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,blk,blk,blk,blk,blk,blk,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    blk,pix,pix,blk,blk,pix,pix,blk,
    ]
]

sense.stick.direction_any = roll

while True:
    gyro = sense.get_accelerometer_raw()
    for i in gyro:
        gyro[i] = round(gyro[i])
    
    if gyro['x'] != 0 or gyro['y'] != 0 or gyro['z'] != 1:
        roll()
