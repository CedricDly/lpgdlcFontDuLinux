# -*- coding: utf-8 -*-
import socket
import servo
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 6667

def getAngle(str):
	return -45

socket.bind(('', PORT))
socket.listen(1)
client, address = socket.accept()
print "{} connected".format( address )

while True:
	data = client.recv(128)
	data_string = data.decode("utf-8")
	print "RECU : {}".format(data_string)
	if data_string:
		servo.changeCycle(data_string)
	
	elif not data_string:
		print "NOTHING BREAK"
		break

print "Close"
client.close()
socket.close()
servo.closePWM()
