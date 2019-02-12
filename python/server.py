# -*- coding: utf-8 -*-
import socket
import servo

# Constants
BUFFER_SIZE = 128

# Creating the socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 6667

# Binding the socket to the port
socket.bind(('', PORT))

# Awaiting a connection
socket.listen(1)

# Accepting the connection
client, address = socket.accept()
print "{} connected".format( address )

while True:
	# Receiving data of maximum size of BUFFER_SIZE
	data = client.recv(BUFFER_SIZE)
	data_string = data.decode("utf-8")
	print "RECU : {}".format(data_string)

	# Translating commands
	if data_string:
		servo.changeCycle(data_string)
	
	# If no command, exit
	elif not data_string:
		print "EXIT"
		break

# Stops the server correctly
print "Close"
client.close()
socket.close()
servo.closePWM()
