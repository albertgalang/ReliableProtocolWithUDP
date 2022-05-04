import socket
import UDPServer
import TCPServer

IP = socket.gethostbyname(socket.gethostname())  # (localhost)
SERVER_PORT = 4455  # Port to listen on (non-privileged ports are > 1023)
ADDR = (IP, SERVER_PORT)
SIZE = 1024
FORMAT = "utf-8"


def main():
    # TCP: start server to listen for connections.
    #      A client will establish a connection and send necessary
    #      information regarding the file being sent such as file
    #      name and the SHA256 value to be checked later.
    #      In the event that the received information such as file name
    #      and the SHA256 are empty, the socket will remain open. The server
    #      will wait for the client to send again.
    filename, hash_message = TCPServer.start_server(ADDR, FORMAT, SIZE)

    # UDP: Start server and listen for incoming datagrams.
    #      The SHA256 of the acquired data is taken.
    #      The acquired data SHA256 is checked against the SHA256 hash_message
    #      value received in the TCP transfer. A match means the packets
    #      were sent reliably.
    #      In the even that the packets are not received reliably, the UDP socket
    #      remains open and will wait for the client to resend the data.
    message = UDPServer.start_server(ADDR, FORMAT, SIZE, hash_message)
    fileWrite = open('received.txt', 'wb')
    fileWrite.write(message)


if __name__ == "__main__":
    main()
