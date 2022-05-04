import socket

def start_server(ADDR, FORMAT, SIZE):

    # TCP
    print("[STARTING] TCP Server is starting.")

    # Starting TCP Connection
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Starting the socket
    server.bind(ADDR)  # Bind the IP and SERVER_PORT to the server
    server.listen()  # Server is listening(waiting for client)

    print("[LISTENING] TCP Server is listening.")

    while True:
        # Server has accepted the connection from the client.
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        # file name
        filename = conn.recv(SIZE).decode(FORMAT)  # Recieving the filename from the client.
        print(f"[RECV] Receiving the filename.")
        conn.send("Filename recieved.".encode(FORMAT))
        print(f"Filename: {filename}")

        # hash message
        hash_message = conn.recv(SIZE).decode(FORMAT)  # Received hash message
        print(f"[RECV] Receiving the hash message.")
        conn.send("hash message received.".encode(FORMAT))
        print(f"hash message: {hash_message}")

        conn.close()  # Closing the connection from the client.

        print(f"[DISCONNECTED] {addr} disconnected.")

        if bool(filename) and bool(hash_message):
            return filename, hash_message