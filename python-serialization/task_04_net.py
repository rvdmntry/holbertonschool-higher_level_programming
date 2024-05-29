#!/usr/bin/python3
import socket
import json


def start_server():
    """
    Starts the server to listen for incoming
    connections, receive a serialized dictionary,
    deserialize it, and print the dictionary.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)

    print("Server is listening on port 65432...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024)
    if data:
        received_dict = json.loads(data.decode('utf-8'))
        print("Received Dictionary from Client:")
        print(received_dict)

    conn.close()
    server_socket.close()
