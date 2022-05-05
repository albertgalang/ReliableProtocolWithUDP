import socket
import UDPClient
import TCPClient
import checkFile
import sys

IP = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT = 4455  # The port used by the server
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():
	print("Make sure the server is listening before entering the file name!")
	filename = input("Enter the file name that you want transfered: ")
	result = checkFile.checkFile(filename)
	# TCP: The client will initiate a connection to the server.
	#      As part of the protocol, the client will send the file information
	#      after a connection is established. File name and its SHA256 value
	#      is sent.
	if(result == True):
		TCPClient.send(ADDR, FORMAT, SIZE, filename)
	else:
		sys.exit()

	file = open(filename, "r")  # Opening and reading the file data.
	data = file.read()
	file.close()  # Closing the file

	# UDP: The client will send the file to the server after the TCP procedures.
	#      After sending the data, the server will check the acquired data's
	#      SHA256 value with the other value sent using the TCP protocol.
	#      A match will mean the packets were sent reliably.
	#      In the event that there is no match, the client will resend the data
	#      to the server.
	UDPClient.send(ADDR, FORMAT, SIZE, data)


if __name__ == "__main__":
	main()
