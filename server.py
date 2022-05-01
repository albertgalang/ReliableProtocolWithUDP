import socket
import os
import hashlib
import UDPServer


def hash_file(filename):  # This is a function to get the hash name of the file that is sent over. This might have to be used in the server? I'm not sure but it grabs the hash name for the file and I have it outputing just to see that it is working.
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
# f = open('received.txt', 'w')

def main():

	print("[STARTING] Server is starting.")
	#Starting TCP Connection
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Starting the socket
	server.bind(ADDR) #Bind the IP and SERVER_PORT to the server
	server.listen() #Server is listening(waiting for client)

	print("[LISTENING] Server is listening.")

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


		# write_to_file = 'received.txt'
		# file = open(write_to_file, "w")

		# recieving file data from the client
		# data = conn.recv(SIZE).decode(FORMAT)

		# print(f"[RECV] Receiving the file data. : ", data)

		# file.write(data)
		#
		# conn.send("File data received.".encode(FORMAT))
		#
		# file.close() #Closing the file

		conn.close() #Closing the connection from the client.

		print(f"[DISCONNECTED] {addr} disconnected.")



		# UDP
		UDP_server = UDPServer.start_server(ADDR, SIZE)

		buffer_in_address = UDP_server.recvfrom(SIZE)

		message = buffer_in_address[0]
		address = buffer_in_address[1]

		client_message = "Message from client : {}".format(message)
		client_address = "Client IP address : {}".format(address)

		print(message)
		print(client_message)
		print(client_address)

		# reliable UDP check
		hash_data = hash_file(filename=filename)
		print(f"Hash data: {hash_data}")

		if hash_data == hash_message:
			print("Packets received in order!")

		#UDP_server.sendto()

	# while (True):
	# 	buffer_in_address = UDP_server.recvfrom(buffer_size)
	#
	# 	message = buffer_in_address[0]
	# 	address = buffer_in_address[1]
	#
	# 	client_message = "Message from client : { }".format(message)
	# 	client_address = "Client IP address : { }".format(address)
	#
	# 	print(message)
	# 	print(client_message)
	# 	print(client_address)
	#
	# 	# reliable UDP check
	# 	hash_data = hash_file(filename=write_to_file)
	# 	print(f"Hash data: {hash_data}")
	#
	#
	# 	UDP_server.sendto()

main()


