import chess

# Create a chess board object
board = chess.Board()

# Function to display the board
def display_board():
    print(board)

# Function to handle user input
def get_user_move():
    move_input = input("Enter your move in algebraic notation (e.g., e2e4): ")
    try:
        move = chess.Move.from_uci(move_input)
        if move in board.legal_moves:
            return move
        else:
            print("Invalid move. Please try again.")
            return None
    except ValueError:
        print("Invalid move format. Please enter in algebraic notation.")
        return None

# Function to play the game
def play_game():
    display_board()

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            player = "White"
        else:
            player = "Black"

        move = get_user_move()

        if move is not None:
            board.push(move)
            display_board()

            if board.is_checkmate():
                print(f"Checkmate! {player} wins!")
                break
            elif board.is_check():
                print(f"Check!")

# Start the game
play_game()