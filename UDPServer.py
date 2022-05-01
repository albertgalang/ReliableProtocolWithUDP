import socket

def start_server(ADDR, buffer_size):

    # server side UDP socket
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # bind the IP address and port
    server.bind(ADDR)

    print("UDP server is listening...")

    return server
