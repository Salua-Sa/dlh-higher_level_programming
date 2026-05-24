#!/usr/bin/python3
"""Client-server serialization using JSON and sockets"""

import socket
import json


HOST = "127.0.0.1"
PORT = 12345


def start_server():
    """Set up a server socket to listen for incoming connections on a
    specific port. Read the serialized data. Deserialize the data using
    the json module. Print the received dictionary. Close the connection."""
    with socket.socket() as server:
        server.bind((HOST, PORT))
        server.listen(1)
        conn, addr = server.accept()
        data = conn.recv(1024)
        dictionary = json.loads(data.decode())
        print("The received Dictionary from Client is:", dictionary)
    conn.close()
    server.close()


def send_data(data):
    """Establish a connection to the server. Serialize a Python dictionary.
    Send the serialized data to the server. Close the connection."""
    with socket.socket() as client:
        client.connect((HOST, PORT))
        json_data = json.dumps(data)
        client.send(json_data.encode())
    client.close()
