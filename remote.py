#!/usr/bin/env python  
import socket
import serial
import time

def main():
  host = '192.168.1.53'
  port = 4000
  backlog = 10
  bufsize = 4096
  
  commseq = 0
########################setup serial
  ser = serial.Serial('/dev/ttyUSB0' , 115200)
########################
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  sock.bind((host, port))
  sock.listen(backlog)
  conn,address = sock.accept()
  
  comm.send("+++++ MARS ROVER CONSOLE +++++\r\n")
  
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
        rep = "Dummy Data"
        if rep:
            conn.send("[" + str(commseq) + "] " + rep + "\r\n") #send report to host
            print(rep) #monitoring report
        #conn.send(msg)
        commseq += 1
  conn.close()

if __name__ == '__main__':
  main()
