import socket
import os
import hashlib
import UDPClient
import TCPClient

IP = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT = 4455  # The port used by the server
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
	# TCP
	TCPClient.send(ADDR, FORMAT, SIZE)

	# UDP
	file = open("test.txt", "r") #Opening and reading the file data.
	data = file.read()
	file.close() #Closing the file
	UDPClient.send(ADDR, FORMAT, SIZE, data)


if __name__ == "__main__":
	main()


