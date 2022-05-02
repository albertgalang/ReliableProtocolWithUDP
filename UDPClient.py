import socket
import os

def send(ADDR, FORMAT, SIZE, data):

    # client side UDP socket
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    client_socket.sendto(data.encode(FORMAT), ADDR)

    msg_from_server = client_socket.recvfrom(SIZE).decode(FORMAT)
    

    return "Message from server: { }".format(msg_from_server[0])



