import socket

import hash_sha


def start_server(ADDR, FORMAT, SIZE, HASH_CHECK):

    # UDP
    print("\n[STARTING] UDP Server is starting")

    # server side UDP socket
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # bind the IP address and port
    server.bind(ADDR)

    print("[LISTENING] UDP server is listening...")

    while True:
        print(f"[NEW CONNECTION] {ADDR} connected.")
        buffer_in_address = server.recvfrom(SIZE)

        message = buffer_in_address[0]
        address = buffer_in_address[1]

        # client_message = "Message from file : {}".format(message)
        # client_address = "Client IP address : {}".format(address)
        #
        # print(client_message)
        # print(client_address)

        # reliable UDP check
        hash_data = hash_sha.get_sha(message.decode(FORMAT))
        print(f"Hash data: {hash_data}")

        print("Checking hash data from file too see if they match.")
        if hash_data == HASH_CHECK:
            print("Hashes Match! Packets received reliably!")
            server.sendto("Hashes Match! Packets received reliably!".encode(FORMAT), address)
            return message
        else:
            print("Hashes don't Match! Packets NOT received reliably!")
            server.sendto("Hashes don't Match! Packets NOT received reliably!".encode(FORMAT), address)
