#!/usr/bin/env python  
import serial
import time

# Open serial port
ser = serial.Serial('/dev/ttyUSB0' , 115200)

for i in range(1): # loop count in range(n)
    # Start sequence
    # Step 1
    print("forward")
    ser.write("f 1000\r")
    # Step 2
    print("Backup")
    ser.write("b 1000\r")

# End of program
