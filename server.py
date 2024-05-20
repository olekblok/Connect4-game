# server.py (Updated)

import socket
import threading
from connect4 import Connect4

class Connect4Server:
    def __init__(self, host='localhost', port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Server started on {host}:{port}")
        self.clients = []
        self.game = Connect4()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Received message: {message}")
                    col = int(message)
                    if self.game.is_valid_location(col):
                        row = self.game.get_next_open_row(col)
                        self.game.drop_piece(row, col)
                        if self.game.winning_move():
                            self.broadcast(f"Player {self.game.current_player} wins!")
                            self.game = Connect4()
                        else:
                            self.game.switch_player()
                            self.broadcast(f"Player {self.game.current_player}'s turn\n{self.game_board_to_string()}")
            except ConnectionResetError:
                break

        client_socket.close()
        self.clients.remove(client_socket)

    def broadcast(self, message):
        for client in self.clients:
            client.send(message.encode('utf-8'))

    def game_board_to_string(self):
        board_str = ""
        for row in self.game.board:
            board_str += '|'.join(row) + "\n"
        board_str += ' '.join([str(i) for i in range(self.game.COLS)])
        return board_str

    def start(self):
        print("Server is running and waiting for connections...")
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            self.clients.append(client_socket)
            client_socket.send(f"Welcome to Connect4! Player {self.game.current_player}'s turn\n{self.game_board_to_string()}".encode('utf-8'))
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    server = Connect4Server()
    server.start()
