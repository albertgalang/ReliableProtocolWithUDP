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
        # received message and address
        print(f"[NEW CONNECTION] {ADDR} connected.")
        buffer_in_address = server.recvfrom(SIZE)

        message = buffer_in_address[0]
        address = buffer_in_address[1]

        # client_message = "Message from file : {}".format(message)
        # client_address = "Client IP address : {}".format(address)
        #
        # print(client_message)
        # print(client_address)

        # reliable UDP check. Check the message SHA256 value against the hash
        # value acquired from the TCP protocol.
        hash_data = hash_sha.get_sha(message.decode(FORMAT))
        print(f"Hash data: {hash_data}")

        # keep server alive at hash value mismatch and wait for the client to
        # resend the data.
        # close the server when packets are sent reliably.
        print("Checking hash data from file too see if they match.")
        if hash_data == HASH_CHECK:
            print("Hashes Match! Packets received reliably!")
            server.sendto("Hashes Match! Packets received reliably!".encode(FORMAT), address)
            server.close()
            return message
        else:
            print("Hashes don't Match! Packets NOT received reliably!")
            server.sendto("False".encode(FORMAT), address)
