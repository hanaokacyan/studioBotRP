#!/usr/bin/env python  
import socket
import serial

def main():
  host = '192.168.1.53'
  port = 4000
  backlog = 10
  bufsize = 4096
########################
  ser = serial.Serial('/dev/ttyUSB0' , 115200)
########################
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  sock.bind((host, port))
  sock.listen(backlog)
  conn,address = sock.accept()
  while True:                                                      
        msg = conn.recv(bufsize)
        if not msg:
            print '! Disconnected'
            break
        print(msg)
        ser.write(msg)

        rep = ser.readline() #read report from robot via serial
        if rep:
            conn.send(rep) #send report char to host
            conn.send('\r')
            print(rep) #monitoring report
        #conn.send(msg)
  conn.close()

if __name__ == '__main__':
  main()
