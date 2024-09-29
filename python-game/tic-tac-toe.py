# Initialize the game board
board = [' ' for _ in range(9)]

# Define the winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

# Define a function to print the game board
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

# Define a function to check if a player has won
def check_win(player):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Define a function to check if the game is a draw
def check_draw():
    return ' ' not in board

# Define a function to handle a player's turn
def player_turn(player):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == ' ':
            board[int(move) - 1] = player
            break
        else:
            print("Invalid move. Try again.")

# Define the main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    while True:
        player_turn('X')
        print_board()
        if check_win('X'):
            print("Player X wins!")
            break
        elif check_draw():
            print("It's a draw!")
            break
        player_turn('O')
        print_board()
        if check_win('O'):
            print("Player O wins!")
            break
        elif check_draw():
            print("It's a draw!")
            break

# Start the game
play_game()
