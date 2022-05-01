import socket
import os
import hashlib
import UDPClient

def hash_file(filename): #This is a function to get the hash name of the file that is sent over. This might have to be used in the server? I'm not sure but it grabs the hash name for the file and I have it outputing just to see that it is working.
	h = hashlib.sha1()
	
	with open(filename, 'rb') as file:
		chunk = 0
		while chunk != b'':
			chunk = file.read(1024)
			h.update(chunk)
	return h.hexdigest() 

IP = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT = 4455  # The port used by the server
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
	#Starting the TCP socket
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR) #Connecting to the server

	# file name
	client.send("test.txt".encode(FORMAT)) #Sending the filename to the server
	msg = client.recv(SIZE).decode(FORMAT) #Updating the server message
	print(f"[SERVER]: {msg}")

	# hash
	hash_message = hash_file("test.txt")
	print(f"Hash Message: {hash_message}") #Here is just an output showing the hash message from the file to show it. But we'll need it to compare it with the UDP transfer.
	client.send(hash_message.encode(FORMAT))
	msg = client.recv(SIZE).decode(FORMAT) #Updating the server message
	print(f"[SERVER]: {msg}")


	client.close() #Closing the connection

	# UDP
	file = open("test.txt", "r") #Opening and reading the file data.
	data = file.read()
	file.close() #Closing the file
	UDPClient.send(ADDR, FORMAT, SIZE, data)





main()


