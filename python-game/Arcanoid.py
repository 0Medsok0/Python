import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game variables
paddle_width, paddle_height = 100, 20
paddle_x, paddle_y = width // 2 - paddle_width // 2, height - paddle_height - 10
ball_radius = 10
ball_x, ball_y = width // 2, height // 2
ball_dx, ball_dy = random.choice([-5, 5]), -5
brick_width, brick_height = 80, 30
bricks = []
for row in range(5):
    for col in range(10):
        bricks.append(pygame.Rect(col * (brick_width + 5) + 5, row * (brick_height + 5) + 5, brick_width, brick_height))

# Define a function to handle game events
def handle_events():
    global paddle_x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += 5

# Define a function to update the game state
def update_game():
    global ball_x, ball_y, ball_dx, ball_dy, bricks
    ball_x += ball_dx
    ball_y += ball_dy
    if ball_x <= ball_radius or ball_x >= width - ball_radius:
        ball_dx = -ball_dx
    if ball_y <= ball_radius:
        ball_dy = -ball_dy
    if ball_y >= height - ball_radius:
        pygame.quit()
        quit()
    if pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height).collidepoint(ball_x, ball_y):
        ball_dy = -abs(ball_dy)
    for brick in bricks:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_dy = -ball_dy
            break

# Define a function to draw the game objects
def draw_game():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)
    for brick in bricks:
        pygame.draw.rect(screen, (255, 0, 0), brick)
    pygame.display.update()

# Define the main game loop
def main():
    while True:
        handle_events()
        update_game()
        draw_game()
        clock.tick(60)

# Start the game
main()
