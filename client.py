# client.py (Updated)

import socket
import threading

class Connect4Client:
    def __init__(self, host='localhost', port=12345):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

    def send_message(self, message):
        self.client_socket.send(message.encode('utf-8'))

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"\n{message}\n> ", end="")
            except ConnectionResetError:
                break

if __name__ == "__main__":
    client = Connect4Client()
    threading.Thread(target=client.receive_messages).start()
    while True:
        message = input("> ")
        client.send_message(message)
