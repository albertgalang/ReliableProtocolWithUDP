import socket
import os

IP = socket.gethostbyname(socket.gethostname())  #(localhost)
SERVER_PORT = 4455  # Port to listen on (non-privileged ports are > 1023)
ADDR = (IP, SERVER_PORT)
SIZE = 1024
FORMAT = "utf-8"

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

		filename = conn.recv(SIZE).decode(FORMAT) #Recieving the filename from the client.

		print(f"[RECV] Receiving the filename.")

		file = open(filename, "w")

		conn.send("Filename recieved.".encode(FORMAT))
		print(f"Filename: {filename}")

		#recieving file data from the client
		data = conn.recv(SIZE).decode(FORMAT)

		print(f"[RECV] Receiving the file data.")

		file.write(data)

		conn.send("File data received.".encode(FORMAT))
		
		file.close() #Closing the file

		conn.close() #Closing the connection from the client.

		print(f"[DISCONNECTED] {addr} disconnected.")
	#This is where I was messing with the UDP stuff kind of lol. It's not that great... it was messing up the code. 
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


