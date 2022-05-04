import socket
import UDPClient
import TCPClient

IP = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT = 4455  # The port used by the server
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():

	# TCP: The client will initiate a connection to the server.
	#      As part of the protocol, the client will send the file information
	#      after a connection is established. File name and its SHA256 value
	#      is sent.
	TCPClient.send(ADDR, FORMAT, SIZE)

	file = open("test.txt", "r")  # Opening and reading the file data.
	data = file.read()
	file.close()  # Closing the file

	# UDP: The client will send the file to the server after the TCP procedures.
	#      After sending the data, the server will check the acquired data's
	#      SHA256 value with the other value sent using the TCP protocol.
	#      A match will mean the packets were sent reliably.
	#      In the event that there is no match, the client will resend the data
	#      to the server.
	UDPClient.send(ADDR, FORMAT, SIZE, data)


if __name__ == "__main__":
	main()


