import socket
import os
import tqdm

HOST = socket.gethostname()  # The server's hostname or IP address
PORT = 65432  # The port used by the server
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
filename = "test.txt"
filesize = os.path.getsize(filename)

s = socket.socket()
print(f"[+] Connecting to {HOST} : {PORT}")
s.connect((HOST, PORT))
print("[+] Connected.")
# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

#start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale = True, unit_divisor = 1024)

with open(filename, "rb") as f:
	while True:
		bytes_read = f.read(BUFFER_SIZE)
		if not bytes_read:
			break
		s.sendall(bytes_read)
		progress.update(len(bytes_read))
s.close()


