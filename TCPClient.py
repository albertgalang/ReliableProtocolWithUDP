import socket
from hash_sha import *

def send(ADDR, FORMAT, SIZE):

	# Starting the TCP socket
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)  # Connecting to the server

	# file name
	client.send("test.txt".encode(FORMAT))  # Sending the filename to the server
	msg = client.recv(SIZE).decode(FORMAT)  # Updating the server message
	print(f"[SERVER]: {msg}")

	# hash
	file = open("test.txt", "r")  # Opening and reading the file data.
	data = file.read()
	hash_message = get_sha(data)
	print(f"Hash Message: {hash_message}")  # Here is just an output showing the hash message
	client.send(hash_message.encode(FORMAT))  # Sending hash message to server
	msg = client.recv(SIZE).decode(FORMAT)  # Updating the server message
	print(f"[SERVER]: {msg}")

