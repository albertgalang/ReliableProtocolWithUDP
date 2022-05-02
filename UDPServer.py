import socket

def start_server(ADDR, SIZE):

    # server side UDP socket
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # bind the IP address and port
    server.bind(ADDR)

    print("[LISTENING] UDP server is listening...")

    return server
