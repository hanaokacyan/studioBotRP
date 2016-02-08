#!/usr/bin/env python  
import serial
import time

# Open serial port
ser = serial.Serial('/dev/ttyUSB0' , 115200)
time.sleep(0.5)

for i in range(2): # loop count in range(n)
    # Start sequence
    # Step 1
    print("forward")
    ser.write("m 1 32 1 32\r") # !!!Replace by your command
    time.sleep(1.0) # dulation 1.0sec
    # Step 2
    print("brake")
    ser.write("m 3 32 3 32\r") # !!!Replace by your command
    time.sleep(0.5) # dulation 0.5sec
    # Step 3
    print("Backup")
    ser.write("m 2 32 2 32\r") # !!!Replace by your command
    time.sleep(1.0) # dulation 1.0sec
    # Step 4
    print("brake")
    ser.write("m 3 32 3 32\r") # !!!Replace by your command
    time.sleep(0.5) # dulation 0.5sec
    
    ser.close()

# End of program
