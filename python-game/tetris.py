import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Определение размеров окна и игрового поля
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Тетрис")

# Определение фигур
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

# Определение цветов фигур
COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (128, 128, 128)
]

# Функция для создания новой фигуры
def new_shape():
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    x = GRID_WIDTH // 2 - len(shape[0]) // 2
    y = 0
    return shape, color, x, y

# Функция для поворота фигуры
def rotate_shape(shape):
    return [list(reversed(row)) for row in zip(*shape)]

# Функция для проверки коллизий
def check_collision(shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] and (x + col < 0 or x + col >= GRID_WIDTH or y + row >= GRID_HEIGHT or grid[y + row][x + col]):
                return True
    return False

# Функция для добавления фигуры в сетку
def add_shape_to_grid(shape, color, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col]:
                grid[y + row][x + col] = color

# Функция для удаления полных строк
def remove_full_rows():
    full_rows = []
    for row in range(GRID_HEIGHT):
        if all(grid[row]):
            full_rows.append(row)
    for row in full_rows:
        del grid[row]
        grid.insert(0, [0] * GRID_WIDTH)

# Создание игрового поля
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Создание первой фигуры
current_shape, current_color, current_x, current_y = new_shape()

# Игровой цикл
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotated_shape = rotate_shape(current_shape)
                if not check_collision(rotated_shape, current_x, current_y):
                    current_shape = rotated_shape

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if not check_collision(current_shape, current_x - 1, current_y):
            current_x -= 1
    if keys[pygame.K_RIGHT]:
        if not check_collision(current_shape, current_x + 1, current_y):
            current_x += 1
    if keys[pygame.K_DOWN]:
        if not check_collision(current_shape, current_x, current_y + 1):
            current_y += 1

    # Падение фигуры
    if not check_collision(current_shape, current_x, current_y + 1):
        current_y += 1
    else:
        add_shape_to_grid(current_shape, current_color, current_x, current_y)
        remove_full_rows()
        current_shape, current_color, current_x, current_y = new_shape()

    # Отрисовка игрового поля
    screen.fill(BLACK)
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col]:
                pygame.draw.rect(screen, grid[row][col], (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, GRAY, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    # Отрисовка текущей фигуры
    for row in range(len(current_shape)):
        for col in range(len(current_shape[0])):
            if current_shape[row][col]:
                pygame.draw.rect(screen, current_color, ((current_x + col) * BLOCK_SIZE, (current_y + row) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, GRAY, ((current_x + col) * BLOCK_SIZE, (current_y + row) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
