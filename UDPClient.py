import socket


def send(ADDR, FORMAT, SIZE, data):

    while True:
        # client side UDP socket
        client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        client_socket.sendto(data.encode(FORMAT), ADDR)

        msg_from_server = client_socket.recvfrom(SIZE)
        print(f"[SERVER]: {msg_from_server[0].decode(FORMAT)}")

        if msg_from_server[0].decode(FORMAT) == "False":
            print("Hashes don't Match! Packets NOT received reliably!")
            print("Resending...")
        else:
            return
