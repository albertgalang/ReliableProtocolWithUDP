import socket
import hashlib

def hash_file(filename): #This is a function to get the hash name of the file. 
	h = hashlib.sha1()
	
	with open(filename, 'rb') as file:
		chunk = 0
		while chunk != b'':
			chunk = file.read(1024)
			h.update(chunk)
	return h.hexdigest() 

def send(ADDR, FORMAT, SIZE):
	#Starting the TCP socket
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR) #Connecting to the server

	# file name
	client.send("test.txt".encode(FORMAT)) #Sending the filename to the server
	msg = client.recv(SIZE).decode(FORMAT) #Updating the server message
	print(f"[SERVER]: {msg}")

	# hash
	hash_message = hash_file("test.txt")
	print(f"Hash Message: {hash_message}") #Here is just an output showing the hash message
	client.send(hash_message.encode(FORMAT)) #Sending hash message to server
	msg = client.recv(SIZE).decode(FORMAT) #Updating the server message
	print(f"[SERVER]: {msg}")

