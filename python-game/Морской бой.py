import random

# Initialize the game board
board = [[' ' for _ in range(10)] for _ in range(10)]

# Define the ships
ships = [(5, 'Carrier'), (4, 'Battleship'), (3, 'Cruiser'), (3, 'Submarine'), (2, 'Destroyer')]

# Define a function to print the game board
def print_board():
    print('  1 2 3 4 5 6 7 8 9 10')
    for i, row in enumerate(board):
        print(chr(65 + i), ' '.join(row))

# Define a function to place the ships on the board
def place_ships():
    for length, name in ships:
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                x = random.randint(0, 10 - length)
                y = random.randint(0, 9)
                if all(board[y][x + i] == ' ' for i in range(length)):
                    for i in range(length):
                        board[y][x + i] = name[0]
                    break
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 10 - length)
                if all(board[y + i][x] == ' ' for i in range(length)):
                    for i in range(length):
                        board[y + i][x] = name[0]
                    break

# Define a function to handle a player's turn
def player_turn():
    while True:
        move = input("Enter your move (e.g. A5): ")
        if len(move) == 2 and move[0].isalpha() and move[1].isdigit() and 1 <= int(move[1:]) <= 10:
            x = ord(move[0].upper()) - 65
            y = int(move[1:]) - 1
            if board[y][x] == ' ':
                board[y][x] = 'O'
                print("Miss!")
                break
            elif board[y][x] == 'X':
                print("You already guessed that spot. Try again.")
            else:
                board[y][x] = 'X'
                print("Hit!")
                break
        else:
            print("Invalid move. Try again.")

# Define a function to check if all ships have been sunk
def check_win():
    return all(ship[0] * ship[0] == sum(row.count(ship[0]) for row in board) for ship in ships)

# Define the main game loop
def play_game():
    print("Welcome to Battleship!")
    place_ships()
    while True:
        print_board()
        player_turn()
        if check_win():
            print("Congratulations! You sank all the ships!")
            break

# Start the game
play_game()

