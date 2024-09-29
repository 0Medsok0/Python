import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game variables
snake_pos = [(width // 2, height // 2)]
snake_dir = (1, 0)
food_pos = (random.randint(0, width // 20 - 1) * 20, random.randint(0, height // 20 - 1) * 20)
score = 0

# Define a function to handle game events
def handle_events():
    global snake_dir
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, 1):
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -1):
                snake_dir = (0, 1)
            elif event.key == pygame.K_LEFT and snake_dir != (1, 0):
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-1, 0):
                snake_dir = (1, 0)

# Define a function to update the game state
def update_game():
    global snake_pos, food_pos, score
    head_x, head_y = snake_pos[0]
    dir_x, dir_y = snake_dir
    new_head = (head_x + dir_x * 20, head_y + dir_y * 20)
    if new_head == food_pos:
        score += 1
        food_pos = (random.randint(0, width // 20 - 1) * 20, random.randint(0, height // 20 - 1) * 20)
    else:
        snake_pos.pop()
    snake_pos.insert(0, new_head)
    if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height or new_head in snake_pos[1:]:
        pygame.quit()
        quit()

# Define a function to draw the game objects
def draw_game():
    screen.fill((0, 0, 0))
    for x, y in snake_pos:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), (food_pos[0], food_pos[1], 20, 20))
    pygame.display.update()

# Define the main game loop
def main():
    while True:
        handle_events()
        update_game()
        draw_game()
        clock.tick(10)

# Start the game
main()
