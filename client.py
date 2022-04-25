import socket
import os
import hashlib

def hash_file(filename):
	h = hashlib.sha1()
	
	with open(filename, 'rb') as file:
		chunk = 0
		while chunk != b'':
			chunk = file.read(1024)
			h.update(chunk)
	return h.hexdigest()

IP = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT = 65432  # The port used by the server
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	client.connect(ADDR)

	file = open("test.txt", "r")

	data = file.read()

	client.send("test.txt".encode(FORMAT))

	msg = client.recv(SIZE).decode(FORMAT)

	print(f"[SERVER]: {msg}")

	file.close()
	client.close()

	#client_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	#client_UDP.connect(ADDR)

	#file = open("test.txt", "r")
	
	#data = file.read()

	#client.send("test.txt".encode(FORMAT))

	#msg = client.recv(SIZE).decode(FORMAT)

	#print(f"[SERVER]: {msg}")

	#file.close()
	#client_UDP.close()


	hash_message = hash_file("test.txt")
	print(f"Hash Message: {hash_message}")

main()


