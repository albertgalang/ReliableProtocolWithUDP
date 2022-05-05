import socket
from hash_sha import *

def send(ADDR, FORMAT, SIZE, filename):

	# Starting the TCP socket
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)  # Connecting to the server

	# send file name
	client.send(filename.encode(FORMAT))  # Sending the filename to the server
	msg = client.recv(SIZE).decode(FORMAT)  # Updating the server message
	print(f"[SERVER]: {msg}")

	# send file hash
	file = open(filename, "r")  # Opening and reading the file data.
	data = file.read()
	hash_message = get_sha(data)
	print(f"Hash Message: {hash_message}")  # Here is just an output showing the hash message
	client.send(hash_message.encode(FORMAT))  # Sending hash message to server
	msg = client.recv(SIZE).decode(FORMAT)  # Updating the server message
	print(f"[SERVER]: {msg}")

