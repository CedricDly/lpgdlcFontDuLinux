# -*- coding: utf-8 -*-
import socket
import servo
import signal

# Constants
BUFFER_SIZE = 128
PORT 		= 6667

def closeSocket(signum, stack):
	"""
	Closing the server
	"""
	servo.stopPWM()
	client.close()
	socket.close()

# Handling the signals
signal.signal(signal.SIGINT, closeSocket)
signal.signal(signal.SIGTERM, closeSocket)
signal.signal(signal.SIGQUIT, closeSocket)
signal.signal(signal.SIGTSTP, closeSocket)

if __name__ == "__main__":
	# Creating the socket
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Binding the socket
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
	closeSocket(client, socket, servo)