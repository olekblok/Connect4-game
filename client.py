# client.py (Updated)

import socket
import threading

class Connect4Client:
    """Client class for Connect 4 game."""
    def __init__(self, host='localhost', port=12345) -> None:
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

    def send_message(self, message) -> None:
        """Send message to server.

        Args:
            message (str): String message to send to server.
        """
        self.client_socket.send(message.encode('utf-8'))

    def receive_messages(self) -> None:
        """Receive messages from server."""
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
