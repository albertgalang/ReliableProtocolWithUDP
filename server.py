import socket
import os
import tqdm

SERVER_HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
SERVER_PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
#accept connection if there is any
client_socket, address = s.accept()
#if below code is execusted, that means the sender is connected
print(f"[+] {address} is connected.")

#recieve the file infos
#recieve using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename,filesize = received.split(SEPARATOR)

#remove absolute path if there is
filename = os.path.basename(filename)
#convert to int
filesize = int(filesize)

#start receiving the file from the socket and write to file stream
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "wb") as f:
	while True:
		bytes_read = client_socket.recv(BUFFER_SIZE)
		if not bytes_read:
			break
		f.write(bytes_read)
		progress.update(len(bytes_read))

client_socket.close()

s.close()
