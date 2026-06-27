#!/usr/bin/env python3
"""
Tic-Tac-Toe Game
A clean, modular implementation to practice atomic commits.
"""

# ============================================================
# STEP 1: Create this file first with only the code till here + Function 1
# Then follow the commit command below.
# ============================================================


def create_board():
    """Create and return a fresh 3x3 Tic-Tac-Toe board."""
    
    return board


# ============================================================
# ✅ COMMIT POINT 1
# Run these commands:
#
# git add tic_tac_toe.py
# git commit -m "feat: add create_board function"
# ============================================================


def print_board(board):
    """Print the current board in a nice format."""
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")
    print("\n")


# ============================================================
# ✅ COMMIT POINT 2
#
# git add tic_tac_toe.py
# git commit -m "feat: add print_board function"
# ============================================================


def check_winner(board, player):
    """Check if the given player has won."""
    # Check rows
    

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    

    return False


# ============================================================
# ✅ COMMIT POINT 3
#
# git add tic_tac_toe.py
# git commit -m "feat: add check_winner function"
# ============================================================


def is_board_full(board):
    """Check if the board is full (draw condition)."""
    
    return True


# ============================================================
# ✅ COMMIT POINT 4
#
# git add tic_tac_toe.py
# git commit -m "feat: add is_board_full function"
# ============================================================


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
            print("Invalid input. Please enter two numbers separated by space (e.g., 0 1).")


# ============================================================
# ✅ COMMIT POINT 5
#
# git add tic_tac_toe.py
# git commit -m "feat: add get_move function with input validation"
# ============================================================


def play_game():
    """Main function to run the Tic-Tac-Toe game."""
    

# ============================================================
# ✅ COMMIT POINT 6
#
# git add tic_tac_toe.py
# git commit -m "feat: add play_game main game loop"
# ============================================================


if __name__ == "__main__":
    play_game()


# ============================================================
# ✅ FINAL COMMIT (Optional but recommended)
#
# git add tic_tac_toe.py
# git commit -m "feat: complete Tic-Tac-Toe game with replay option"
# ============================================================