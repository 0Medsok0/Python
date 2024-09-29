import random

# Set up the game board
width, height = 10, 10
num_mines = 10
board = [[0] * width for _ in range(height)]
mines = set()
while len(mines) < num_mines:
    x, y = random.randint(0, width - 1), random.randint(0, height - 1)
    mines.add((x, y))
    board[y][x] = -1
for x, y in mines:
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (x + dx, y + dy) in mines or not (0 <= x + dx < width and 0 <= y + dy < height):
                continue
            board[y + dy][x + dx] += 1

# Define a function to print the game board
def print_board(revealed):
    for y in range(height):
        for x in range(width):
            if not revealed[y][x]:
                print('-', end=' ')
            elif board[y][x] == -1:
                print('*', end=' ')
            else:
                print(board[y][x], end=' ')
        print()

# Define a function to handle a player's turn
def play_turn(revealed):
    while True:
        x, y = map(int, input('Enter x and y coordinates (0-9): ').split())
        if not (0 <= x < width and 0 <= y < height) or revealed[y][x]:
            print('Invalid move. Try again.')
        else:
            break
    if board[y][x] == -1:
        print('Game over!')
        return False
    else:
        reveal(x, y, revealed)
        return True

# Define a function to reveal a tile and its neighbors
def reveal(x, y, revealed):
    if revealed[y][x]:
        return
    revealed[y][x] = True
    if board[y][x] == 0:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= x + dx < width and 0 <= y + dy < height:
                    reveal(x + dx, y + dy, revealed)

# Define the main game loop
def main():
    revealed = [[False] * width for _ in range(height)]
    while True:
        print_board(revealed)
        if not play_turn(revealed):
            break
        if all(all(row) for row in revealed):
            print('Congratulations! You won!')
            break

# Start the game
main()
