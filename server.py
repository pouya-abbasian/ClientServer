#!/usr/bin/python2.7
import socket
print("This is Server Script")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_ip = "192.168.1.7"
sock_port = 8585
sock.bind((sock_ip, sock_port))
sock.listen(10)
print "Waiting For Connect Many Clients!"
while True:
	c, addr = sock.accept()
	fullname = c.recv(1024)
	print(fullname + " Joinded The Server!")
#Send WellCome Message To Client
	c.send("Dear " + fullname)
#Get Firs Message
	while True:
		print(c.recv(1024))
		message = raw_input("You :  ")
		print("Typing ... ")
		c.send("\nServer  :  " + message)
	c.close
