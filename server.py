# server.py

import socket
import threading
from connect4 import Connect4

class Connect4Server:
    def __init__(self, host='localhost', port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(2)  # We need only two clients
        print(f"Server started on {host}:{port}")
        self.clients = []
        self.game = Connect4()
        self.turn = 0  # Track which player's turn it is

    def handle_client(self, client_socket, player):
        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    try:
                        col = int(message)
                        if col < 0 or col >= self.game.COLS:
                            client_socket.send("Invalid move. Column out of range.".encode('utf-8'))
                            continue
                        if not self.game.is_valid_location(col):
                            client_socket.send("Invalid move. Column is full.".encode('utf-8'))
                            continue
                        if self.turn != player:
                            client_socket.send("It's not your turn.".encode('utf-8'))
                            continue
                        row = self.game.get_next_open_row(col)
                        self.game.drop_piece(row, col)
                        if self.game.winning_move():
                            self.broadcast(f"Player {self.game.current_player} wins!")
                            self.game = Connect4()  # Reset the game
                        else:
                            self.game.switch_player()
                            self.turn = 1 - self.turn  # Switch turn
                            self.broadcast(f"Player {self.game.current_player}'s turn\n{self.game_board_to_string()}")
                    except ValueError:
                        client_socket.send("Invalid input. Please enter a valid column number.".encode('utf-8'))
        except ConnectionResetError:
            client_socket.close()
            self.clients.remove(client_socket)
            self.broadcast("A player has disconnected. Game over.")
            self.game = Connect4()  # Reset the game
            print(f"Client {player + 1} disconnected")

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.send(message.encode('utf-8'))
            except BrokenPipeError:
                pass

    def game_board_to_string(self):
        board_str = ""
        for row in self.game.board:
            board_str += '|'.join(row) + "\n"
        board_str += ' '.join([str(i) for i in range(self.game.COLS)])
        return board_str

    def start(self):
        print("Server is running and waiting for connections...")
        while len(self.clients) < 2:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            self.clients.append(client_socket)
            player = len(self.clients) - 1
            client_socket.send(f"Welcome to Connect4! You are player {player + 1}. Player {self.game.current_player}'s turn\n{self.game_board_to_string()}".encode('utf-8'))
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket, player))
            client_handler.start()

if __name__ == "__main__":
    server = Connect4Server()
    server.start()
