# -*- coding: utf-8 -*-
import signal, socket, servo

# Constants
BUFFER_SIZE = 128
PORT 		= 6667

def closeSocket(signum, stackframe):
	"""
	Closing the server
	"""
	servo.stopPWM()
	client.close()
	socket.close()

if __name__ == "__main__":
	# Creating the socket
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Binding the socket
	socket.bind(('', PORT))

	# Awaiting a connection
	socket.listen(1)

	# Accepting the connection
	client, address = socket.accept()
	print "{} connected".format(address)

	# Handling the signals
	# Ctrl + c
	signal.signal(signal.SIGINT, closeSocket)
	
	# Ctrl + \
	signal.signal(signal.SIGQUIT, closeSocket)
	
	# Ctrl + z
	signal.signal(signal.SIGTSTP, closeSocket)

	# Sent in the command line (ex : killall python)
	signal.signal(signal.SIGTERM, closeSocket)

	while True:
		# Receiving data of maximum size of BUFFER_SIZE
		data = client.recv(BUFFER_SIZE)
		data_string = data.decode("utf-8")

		# Transmitting commands
		if data_string:
			try:
				servo.changeCycle(data_string)
			
			except servo.InvalidServoCommand as invalid:
				# Printing the error message.
				# The loop is not broken by invalid commands.
				print invalid.message
		
		# If no command, exit
		elif not data_string:
			print "NO COMMAND"
			break

	# Stops the server correctly
	print "Closing ..."
	closeSocket(client, socket, servo)
	print "Closed"