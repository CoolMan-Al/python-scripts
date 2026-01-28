#!/usr/bin/python3
from bme280 import load_calibration_params, sample
from smbus2 import SMBus
from time import sleep

#How to use the BME280 Air sensor

#Initialise Sensor and Bus
address = 0x76 #0x76 or 0x77
bus = SMBus(1)

#Variable to hold readings
sensor = sample(bus,address)

while True:
    print('Temp:', int(sensor.temperature), 'C', '| Humidity:', int(sensor.humidity), 'hPA', '| Pressure:', int(sensor.pressure), '%')
    sleep(1)