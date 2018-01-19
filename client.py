#!/usr/bin/python2.7
import socket
print("This is Client Script")
##Get User Name
fname = raw_input("Enter Your Name : ")
lname = raw_input("Enter Your Last-Name : ")
fullname = fname+ " "+lname
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_ip = "pouyaserver.duckdns.org"
sock_port = 8585
##Connect Command
sock.connect((sock_ip, sock_port))
sock.send(fullname)
#WellCome Message From Server
print(sock.recv(1024) + " WellCome To " + sock_ip + " Server!")
#Firs Message From Clients
while True:
	message = raw_input("You  :  ")
	print("Typing ... ")
	sock.send(fname +"  :  "+ message)
	print(sock.recv(1024))
