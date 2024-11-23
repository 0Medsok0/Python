import pygame
import sys

# Инициализация pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 300, 300
CELL_SIZE = 100

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики нолики')

# Игровая сетка
grid = [[None for _ in range(3)] for _ in range(3)]

# Функция для рисования сетки
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

# Функция для рисования крестиков и ноликов
def draw_marks():
    for x in range(3):
        for y in range(3):
            if grid[x][y] == 'X':
                pygame.draw.line(screen, RED, (x * CELL_SIZE + 10, y * CELL_SIZE + 10),
                                 ((x + 1) * CELL_SIZE - 10, (y + 1) * CELL_SIZE - 10), 5)
                pygame.draw.line(screen, RED, ((x + 1) * CELL_SIZE - 10, y * CELL_SIZE + 10),
                                 (x * CELL_SIZE + 10, (y + 1) * CELL_SIZE - 10), 5)
            elif grid[x][y] == 'O':
                pygame.draw.circle(screen, BLUE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2 - 10, 5)

# Функция для проверки победителя
def check_winner():
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] is not None:
            return grid[0][col]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] is not None:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] is not None:
        return grid[0][2]
    return None

# Основной игровой цикл
current_player = 'X'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            x, y = mouseX // CELL_SIZE, mouseY // CELL_SIZE
            if grid[x][y] is None:
                grid[x][y] = current_player
                winner = check_winner()
                if winner:
                    print(f'Победитель: {winner}')
                    running = False
                current_player = 'O' if current_player == 'X' else 'X'

    screen.fill(BLACK)
    draw_grid()
    draw_marks()
    pygame.display.flip()

pygame.quit()
sys.exit()
