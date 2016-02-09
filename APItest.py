#!/usr/bin/env python  
import serial
import time

def motor(Rdir,Rpwm,Ldir,Lpwm):
  #ser.flushInput() # clear serial receve buffer 
  ser.write("m " + str(Rdir) + " " + str(Rpwm) + " "+ str(Ldir) + " " + str(Lpwm) + "\r")  #send command to robot
  dummy = ser.readline() # wait for robot response
  
def brake(dur):
  #ser.flushInput() # clear serial receve buffer
  ser.write("b " + str(dur) + "\r")
  dummy = ser.readline() # wait for robot response

def sensorALL():
  #ser.flushInput() # clear serial receve buffer 
  ser.write("1\r")
  l = int(ser.readline()) # read Left sensor
  ser.write("2\r")
  f = int(ser.readline()) # read Front sensor
  ser.write("3\r")
  r = int(ser.readline()) # read Return sensor
  return(l,f,r)

def main():
  global ser
  ser = serial.Serial('/dev/ttyUSB0' , 115200 , timeout = 0.5)
  
  #dummy data send(To activate USBserial device)
  ser.write("?\r")
  time.sleep(0.1)
  
  #motor(1,20,1,20)
  #time.sleep(1)
  #brake(500)
  #motor(2,20,2,20)
  #time.sleep(1)
  #brake(500)
  #print("end fo program")
  
  while True:
    l,f,r = sensorALL()
    print("SENSOR  " + str(l) + " : " + str(f) + " : " + str(r))
    time.sleep(0.3)
  

if __name__ == '__main__':
  main()
