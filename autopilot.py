#!/usr/bin/env python  
import serial
import time

# Open serial port
ser = serial.Serial('/dev/ttyUSB0' , 115200)

for i in range(1): # loop count in range(n)
    # Start sequence
    # Step 1
    print("forward")
    ser.write("f 0 1\r")
    time.sleep(1.0) # dulation 1.0sec
    # Step 2
    print("brake")
    ser.write("s 0 1\r")
    time.sleep(0.5) # dulation 0.5sec
    # Step 3
    print("Backup")
    ser.write("b 1000\r")
    time.sleep(1.0) # dulation 1.0sec
    # Step 4
    print("brake")
    ser.write("s 0 1\r")
    time.sleep(0.5) # dulation 0.5sec

# End of program
