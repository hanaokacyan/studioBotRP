#!/usr/bin/env python  
import socket
import serial
import time

def main():
  host = '0.0.0.0'
  port = 4000
  backlog = 10
  bufsize = 4096
  commseq = 0 #command sequence
########################setup serial
  ser = serial.Serial('/dev/ttyUSB0' , 115200)
########################
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  sock.bind((host, port))
  sock.listen(backlog)
  conn,address = sock.accept()
  
  print("Starting control-------\r\n") #startup message to pyton control
  conn.send("+++++ STUDIOBOT MARS ROVER CONSOLE +++++\r\n") #startup messege to robot console
  
  while True:                                                      
        msg = conn.recv(bufsize)
        if not msg:
            print '! Disconnected'
            break
        print(msg)
        conn.send("[" + str(commseq) + "] " + msg + "\r\n" ) #feedback command
        ser.flushInput() #clear serial receve buffer 
        ser.write(msg) #send command to robot
        
        #rep = ser.readline() #read report from robot via serial
        rep = "dummy data"
        if rep:
            conn.send("[" + str(commseq) + "] " + rep + "\r\n") #send report to host
            print(rep) #monitoring report

        commseq += 1 #incriment command sequence
  conn.close()

if __name__ == '__main__':
  main()
