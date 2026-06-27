#!/usr/bin/env python3
"""
Tic-Tac-Toe Game
A clean, modular implementation to practice atomic commits.
"""


def create_board():
    """Create and return a fresh 3x3 Tic-Tac-Toe board."""
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    return board


def print_board(board):
    """Print the current board in a nice format."""
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")
    print()


def check_winner(board, player):
    """Check if the given player has won."""

    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check main diagonal
    if all(board[i][i] == player for i in range(3)):
        return True

    # Check opposite diagonal
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    """Check if the board is full (draw condition)."""
    for row in board:
        if ' ' in row:
            return False
    return True


def get_move(board, player):
    """Get a valid move from the player."""
    while True:
        try:
            move = input(f"Player {player}, enter your move (row col): ").strip()
            row, col = map(int, move.split())

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Row and column must be between 0 and 2.")
                continue

            if board[row][col] != ' ':
                print("That cell is already taken. Try again.")
                continue

            return row, col

        except ValueError:
            print("Invalid input! Enter row and column like: 0 2")


def play_game():
    """Main function to run the Tic-Tac-Toe game."""

    board = create_board()
    current_player = 'X'

    print("========== TIC TAC TOE ==========")
    print("Rows and Columns are numbered 0 to 2")
    print("Example move: 1 2")
    print()

    while True:

        print_board(board)

        row, col = get_move(board, current_player)
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} Wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("🤝 It's a Draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()