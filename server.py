import socket
import os

IP = socket.gethostbyname(socket.gethostname())  # Standard loopback interface address (localhost)
SERVER_PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
ADDR = (IP, SERVER_PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():

	print("[STARTING] Server is starting.")

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(ADDR)
	server.listen()

	print("[LISTENING] Server is listening.")

	while True:

		conn, addr = server.accept()

		print(f"[NEW CONNECTION] {addr} connected.")

		filename = conn.recv(SIZE).decode(FORMAT)

		print(f"[RECV] Receiving the filename.")

		file = open(filename, "w")

		conn.send("Filename recieved.".encode(FORMAT))

		data = conn.recv(SIZE).decode(FORMAT)

		print(f"[RECV] Receiving the file data.")

		file.write(data)

		conn.send("File data received.".encode(FORMAT))

		file.close()

		conn.close()

		print(f"[DISCONNECTED] {addr} disconnected.")
	
	#UDP_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	#UDP_server.bind(ADDR)
	
	#print("[LISTENING] UDP Server is listening.")

	#while(True):
		#conn, addr = server.accept()

		#print(f"[NEW CONNECTION] {addr} connected.")

		#filename = conn.recv(SIZE).decode(FORMAT)

		#print(f"[RECV] Recieving the filename.")

		#file = open(filename, "w")

		#conn.send("Filename recieved.".encode(FORMAT))

		#data = conn.recv(SIZE).decode(FORMAT)

		#print(f"[RECV] Receiving the file data.")

		#file.write(data)

		#conn.send("File data received.".encode(FORMAT))

		#file.close()

		#conn.close()

		#print(f"[DISCONNECTED] {addr} disconnected.")
		
		

main()


