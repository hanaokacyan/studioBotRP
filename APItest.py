#!/usr/bin/env python  
import serial
import time

def motor(Rdir,Rpwm,Ldir,Lpwm):
  ser.flushInput() # clear serial receve buffer 
  ser.write("m " + str(Rdir) + " " + str(Rpwm) + " "+ str(Ldir) + " " + str(Lpwm) + "\r")  #send command to robot
  dummy = ser.readline() # wait for robot response
  
def brake(dur):
  ser.flushInput() # clear serial receve buffer
  ser.write("b " + str(dur) + "\r")
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
  global ser
  ser = serial.Serial('/dev/ttyUSB0' , 115200)
  
  motor(1,20,1,20)
  time.sleep(1)
  brake(500)
  moror(2,20,2,20)
  time.sleep(1)
  brake(500)
  print("end fo program")
  
  #while True:
    #l,f,r = sensorALL()
    #print("SENSOR  %d : %d : %d" % (l,f,r))
    #time.sleep(0.3)
  

if __name__ == '__main__':
  main()
