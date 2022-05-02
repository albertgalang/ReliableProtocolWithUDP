import socket
import os
import hashlib
import UDPServer



def hash_file(filename):  # This is a function to get the hash name of the file that is sent over
	h = hashlib.sha1()

	with open(filename, 'rb') as file:
		chunk = 0
		while chunk != b'':
			chunk = file.read(1024)
			h.update(chunk)
	return h.hexdigest()


IP = socket.gethostbyname(socket.gethostname())  #(localhost)
SERVER_PORT = 4455  # Port to listen on (non-privileged ports are > 1023)
ADDR = (IP, SERVER_PORT)
SIZE = 1024
FORMAT = "utf-8"


def main():
	
	#TCP
	print("[STARTING] TCP Server is starting.")
	#Starting TCP Connection
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Starting the socket
	server.bind(ADDR) #Bind the IP and SERVER_PORT to the server
	server.listen() #Server is listening(waiting for client)

	print("[LISTENING] TCP Server is listening.")

	while True:
		#Server has accepted the connection from the client.
		conn, addr = server.accept()
		print(f"[NEW CONNECTION] {addr} connected.")

		# file name
		filename = conn.recv(SIZE).decode(FORMAT) #Recieving the filename from the client.
		print(f"[RECV] Receiving the filename.")
		conn.send("Filename recieved.".encode(FORMAT))
		print(f"Filename: {filename}")

		# hash message
		hash_message = conn.recv(SIZE).decode(FORMAT) # Received hash message
		print(f"[RECV] Receiving the hash message.")
		conn.send("hash message received.".encode(FORMAT))
		print(f"hash message: {hash_message}")

		conn.close() #Closing the connection from the client.

		print(f"[DISCONNECTED] {addr} disconnected.")
		break
		

	# UDP
	print("\n[STARTING] UDP Server is starting")
	
	UDP_server = UDPServer.start_server(ADDR, SIZE)

	UDP_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Starting the socket
	UDP_server.bind(ADDR) #Bind the IP and SERVER_PORT to the server
	

	while True:
		print(f"[NEW CONNECTION] {addr} connected.")
		buffer_in_address = UDP_server.recvfrom(SIZE)

		message = buffer_in_address[0]
		address = buffer_in_address[1]

		client_message = "Message from file : {}".format(message)
		client_address = "Client IP address : {}".format(address)

		print(client_message)
		print(client_address)

		# reliable UDP check
		hash_data = hash_file(filename=filename)
		print(f"Hash data: {hash_data}")
		
		print("Checking hash data from file too see if they match.")
		if hash_data == hash_message:
			print("Hashes Match! Packets received reliably!")
		else:
			print("Hashes don't Match! Packets are not received reliably!")

		fileWrite = open('received.txt', 'wb')
		fileWrite.write(message)
		break



main()


