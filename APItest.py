#!/usr/bin/env python  
import serial
import time

def motor(Rdir,Rpwm,Ldir,Lpwm):
  ser.flushInput() # clear serial receve buffer 
  ser.write("m " + str(Rdir) + " " + str(Rpwm) + " "+ str(Ldir) + " " + str(Lpwm) + "\r")  #send command to robot
  dummy = ser.readline() # wait for robot response

def sensorALL():
  ser.flushInput() # clear serial receve buffer 
  ser.write("1\r")
  l = int(ser.readline()) # wait for robot response
  ser.write("2\r")
  f = int(ser.readline()) # wait for robot response
  ser.write("3\r")
  r = int(ser.readline()) # wait for robot response
  return(l,f,r)

def main():
  ser = serial.Serial('/dev/ttyUSB0' , 115200)
  global ser
  while True:
    l,f,r = sensorALL()
    print("SENSOR  %d : %d : %d" % (l,f,r))
    time.sleep(300)
  

if __name__ == '__main__':
  main()