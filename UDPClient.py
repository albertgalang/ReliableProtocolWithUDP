import socket
import os

def send(ADDR, format, buffer_size, data):

    # client side UDP socket
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    client_socket.sendto(data.encode(format), ADDR)

    msg_from_server = client_socket.recvfrom(buffer_size)

    return "Message from server: { }".format(msg_from_server[0])



