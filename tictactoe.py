# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Function to print the board
def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

# Function to check for a win
def check_win(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

# Main game loop
current_player = "X"

while True:
    print_board(board)
    print(f"Player {current_player}, it's your turn. Enter a position (0-8): ")
    position = int(input())

    if board[position] == " ":
        board[position] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"
    else:
        print("Position already taken. Try again.")
