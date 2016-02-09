#!/usr/bin/env python  
import socket
import serial
import time

def main():
  ############### socket parameters
  host = '0.0.0.0'
  port = 4000  # impotant !!!!!
  backlog = 10
  bufsize = 4096
  #--------------------------------
  commseq = 0 #command sequence 
  # setup serial
  ser = serial.Serial('/dev/ttyUSB0' , 115200 , timeout = 30000)
  ser.write("\r")

  print("waiting for connection...\r\n") # waiting messege to pyton terminal
  ##################################################################### socket connection
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  sock.bind((host, port))
  sock.listen(backlog)
  conn,address = sock.accept() # waiting for connection. "conn" is socket connection object.
  #---------------------------------------------------------------------------------------
  
  print("Starting control\r\n") #startup message to pyton terminal
  
  ################################################################### Sending to socket
  conn.send("+++++ STUDIOBOT MARS ROVER CONSOLE +++++\r\n") # startup messege to robot console
  #------------------------------------------------------------------------------------
  
  while True:   
        ####################### Receve from socket(terminal sends data by line.)
        msg = conn.recv(bufsize) # waiting for messege via socket connection
        #-----------------------------------------------------------------------
        if not msg:
            print '! Disconnected'
            break
        print(msg)
        ######################################################## Send to socket
        conn.send("[" + str(commseq) + "] " + msg + "\r\n" ) # feedback command
        #----------------------------------------------------------------------
        
        ser.flushInput() # clear serial receve buffer 
        ser.write(msg) # send command to robot
        rep = ser.readline() #read report from robot via serial
        #rep = "dummy data"
        if rep:
            ################################################################### Send to socket
            conn.send("[" + str(commseq) + "] " + rep + "\r\n") # send report to robot console
            #---------------------------------------------------------------------------------
            print(rep) # monitoring report

        commseq += 1 # incriment command sequence
  ################# Close connetion
  conn.close()
  #--------------------------------

if __name__ == '__main__':
  main()
