
# Connect4 Distributed Processing Project

This Python project aims to implement the classic game of [Connect4](https://www.unco.edu/hewit/pdf/giant-map/connect-4-instructions.pdf) for the Distributed Processing course. The game will utilize distributed processing techniques to enhance performance and scalability.

## Features

- **Distributed Architecture:** The game server handles multiple clients, allowing multiple players to connect and play the game simultaneously.
- **Real-time Communication:** Players can send their moves to the server, which then broadcasts the updated game state to all connected clients.
- **Basic Game Rules Implementation:** The game includes the fundamental rules of Connect4, including valid move checks and win condition detection.

## Components

### 1. Server

The server is responsible for managing the game state and handling communication between clients.

- **File:** `server.py`
- **Description:** Accepts client connections, handles their messages, updates the game state, and broadcasts messages to all connected clients.

### 2. Client

The client connects to the server, sends moves, and receives updates about the game state.

- **File:** `client.py`
- **Description:** Connects to the server, sends player moves, and displays the game state updates received from the server.

### 3. Game Logic

Implements the core logic of Connect4, including the game board, move validation, and win condition checks.

- **File:** `connect4.py`
- **Description:** Contains the Connect4 class that manages the game board, player moves, and win condition checks.

## How to Run the Project

### Prerequisites

- Python 3.x installed on your machine.

### Steps

1. **Clone the Repository:**

   ```sh
   git clone <repository-url>
   cd connect4-distributed-processing
   ```
2. **Start the Server:**
   Open a terminal and run:

   ```sh
   python server.py
   ```
3. **Start the Client(s):**
   Open separate terminals for each player and run the following command in each terminal:

   ```sh
   python client.py
   ```
4. **Play the Game:**

   - Each client will receive the current game board and whose turn it is.
   - Players take turns by entering the column number (0-6) where they want to drop their piece.
   - The server updates the game board and checks for a win after each move, broadcasting the updated state to all clients.
