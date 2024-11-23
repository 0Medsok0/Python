import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
GRID_SIZE = 8
CELL_SIZE = WINDOW_WIDTH // GRID_SIZE

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
BACKGROUND_COLOR = (173, 216, 230)  # Light blue background

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("3 в ряд")

# Инициализация сетки
grid = [[random.choice(COLORS) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Подсчет очков
score = 0
font = pygame.font.Font(None, 36)

def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(screen, grid[row][col], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def check_matches(falling_cells):
    matches = []
    # Проверка горизонтальных матчей
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE - 2):
            if (row, col) in falling_cells or (row, col + 1) in falling_cells or (row, col + 2) in falling_cells:
                if grid[row][col] == grid[row][col + 1] == grid[row][col + 2]:
                    matches.append((row, col))
                    matches.append((row, col + 1))
                    matches.append((row, col + 2))

    # Проверка вертикальных матчей
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE - 2):
            if (row, col) in falling_cells or (row + 1, col) in falling_cells or (row + 2, col) in falling_cells:
                if grid[row][col] == grid[row + 1][col] == grid[row + 2][col]:
                    matches.append((row, col))
                    matches.append((row + 1, col))
                    matches.append((row + 2, col))

    return matches

def gravity():
    falling_cells = []
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE - 1, -1, -1):
            if grid[row][col] == WHITE:
                for r in range(row, 0, -1):
                    grid[r][col] = grid[r - 1][col]
                    falling_cells.append((r, col))
                grid[0][col] = random.choice(COLORS)
                falling_cells.append((0, col))
    return falling_cells

def swap_cells(pos1, pos2):
    grid[pos1[0]][pos1[1]], grid[pos2[0]][pos2[1]] = grid[pos2[0]][pos2[1]], grid[pos1[0]][pos1[1]]

def animate_swap(pos1, pos2):
    start_pos1 = (pos1[1] * CELL_SIZE, pos1[0] * CELL_SIZE)
    start_pos2 = (pos2[1] * CELL_SIZE, pos2[0] * CELL_SIZE)
    end_pos1 = (pos2[1] * CELL_SIZE, pos2[0] * CELL_SIZE)
    end_pos2 = (pos1[1] * CELL_SIZE, pos1[0] * CELL_SIZE)

    for step in range(10):
        screen.fill(BACKGROUND_COLOR)
        draw_grid()
        pygame.draw.rect(screen, grid[pos1[0]][pos1[1]],
                         (start_pos1[0] + (end_pos1[0] - start_pos1[0]) * step / 10,
                          start_pos1[1] + (end_pos1[1] - start_pos1[1]) * step / 10,
                          CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, grid[pos2[0]][pos2[1]],
                         (start_pos2[0] + (end_pos2[0] - start_pos2[0]) * step / 10,
                          start_pos2[1] + (end_pos2[1] - start_pos2[1]) * step / 10,
                          CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        pygame.time.wait(50)

def animate_destroy(matches):
    for step in range(10):
        screen.fill(BACKGROUND_COLOR)
        draw_grid()
        for match in matches:
            pygame.draw.rect(screen, WHITE,
                             (match[1] * CELL_SIZE, match[0] * CELL_SIZE,
                              CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        pygame.time.wait(50)

def main():
    global score
    running = True
    selected_cell = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE
                if selected_cell is None:
                    selected_cell = (row, col)
                else:
                    if (abs(selected_cell[0] - row) + abs(selected_cell[1] - col)) == 1:
                        animate_swap(selected_cell, (row, col))
                        swap_cells(selected_cell, (row, col))
                        matches = check_matches([selected_cell, (row, col)])
                        if matches:
                            animate_destroy(matches)
                            for match in matches:
                                grid[match[0]][match[1]] = WHITE
                            falling_cells = gravity()
                            score += len(matches) * 10
                            # Проверка и уничтожение новых комбинаций после падения
                            while True:
                                matches = check_matches(falling_cells)
                                if not matches:
                                    break
                                animate_destroy(matches)
                                for match in matches:
                                    grid[match[0]][match[1]] = WHITE
                                falling_cells = gravity()
                                score += len(matches) * 10
                        else:
                            swap_cells(selected_cell, (row, col))  # Возврат на место, если нет матчей
                    selected_cell = None

        screen.fill(BACKGROUND_COLOR)
        draw_grid()
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
