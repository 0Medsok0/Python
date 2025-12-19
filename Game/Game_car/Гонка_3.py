import pygame
import time
import random
import os

# --- Инициализация Pygame ---
pygame.init()

# --- Константы (Настройки) ---
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
CAR_WIDTH = 60  # Немного увеличим ширину для спрайтов
CAR_HEIGHT = 120 # Увеличим высоту для спрайтов
FPS = 60

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 0)

# Настройка окна
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Супер 2D Гонки v2.0')
clock = pygame.time.Clock()

# Шрифты
font_small = pygame.font.SysFont("bahnschrift", 25)
font_medium = pygame.font.SysFont("bahnschrift", 40)
font_large = pygame.font.SysFont("bahnschrift", 60)

# --- Загрузка Ассетов (Картинок) с системой заглушек ---

def load_image_asset(filename, width, height, fallback_color):
    """
    Пытается загрузить изображение. Если не находит - создает цветной прямоугольник-заглушку.
    """
    try:
        img = pygame.image.load(filename)
        # Масштабируем под наши размеры
        img = pygame.transform.scale(img, (width, height))
        print(f"Успешно загружен: {filename}")
        return img
    except FileNotFoundError:
        print(f"Файл не найден: {filename}. Использую заглушку.")
        # Создаем заглушку, если картинки нет
        surf = pygame.Surface((width, height))
        surf.fill(fallback_color)
        # Рисуем "фары", чтобы понимать где перед
        pygame.draw.rect(surf, YELLOW, [width*0.1, height*0.05, width*0.2, height*0.1])
        pygame.draw.rect(surf, YELLOW, [width*0.7, height*0.05, width*0.2, height*0.1])
        # Рисуем лобовое стекло
        pygame.draw.rect(surf, (100,100,200), [width*0.1, height*0.2, width*0.8, height*0.2])
        return surf

# Загрузка игрока
player_img = load_image_asset('racecar.png', CAR_WIDTH, CAR_HEIGHT, RED)

# Загрузка врагов (список разных видов)
enemy_images = []
enemy_images.append(load_image_asset('enemy1.png', CAR_WIDTH, CAR_HEIGHT, BLUE))
enemy_images.append(load_image_asset('enemy2.png', CAR_WIDTH, CAR_HEIGHT, GREEN))
enemy_images.append(load_image_asset('enemy3.png', CAR_WIDTH, CAR_HEIGHT, (150, 50, 200))) # Фиолетовый

# Загрузка фона (дороги)
try:
    bg_img = pygame.image.load('road.png')
    bg_img = pygame.transform.scale(bg_img, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
except FileNotFoundError:
    # Создаем процедурный фон, если картинки нет
    bg_img = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    bg_img.fill(GRAY)
    pygame.draw.line(bg_img, WHITE, (DISPLAY_WIDTH/2, 0), (DISPLAY_WIDTH/2, DISPLAY_HEIGHT), 10)
    pygame.draw.line(bg_img, WHITE, (DISPLAY_WIDTH/4, 0), (DISPLAY_WIDTH/4, DISPLAY_HEIGHT), 5)
    pygame.draw.line(bg_img, WHITE, (DISPLAY_WIDTH*0.75, 0), (DISPLAY_WIDTH*0.75, DISPLAY_HEIGHT), 5)
    # Добавим текстуру асфальта точками
    for _ in range(500):
        rx = random.randint(0, DISPLAY_WIDTH)
        ry = random.randint(0, DISPLAY_HEIGHT)
        pygame.draw.circle(bg_img, (70,70,70), (rx, ry), 2)


# --- Функции помощники ---

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, font_type, color, y_offset=0):
    textSurf, textRect = text_objects(text, font_type, color)
    textRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2) + y_offset)
    game_display.blit(textSurf, textRect)

def show_score(score):
    score_surf = font_small.render("Счет: " + str(score), True, YELLOW)
    game_display.blit(score_surf, [10, 10])

def show_speed(speed):
    speed_surf = font_small.render("Скорость: " + str(int(speed*10)) + " км/ч", True, WHITE)
    game_display.blit(speed_surf, [DISPLAY_WIDTH - 250, 10])

# --- Стартовый экран ---
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        game_display.fill(BLACK)
        # Используем фон для меню тоже, но затемненный
        dark_bg = bg_img.copy()
        dark_bg.fill((100, 100, 100), special_flags=pygame.BLEND_RGB_MULT)
        game_display.blit(dark_bg, (0,0))

        message_display("СУПЕР 2D ГОНКИ", font_large, RED, -50)
        message_display("Управление: Стрелки Влево/Вправо", font_small, WHITE, 20)
        message_display("Нажмите ПРОБЕЛ чтобы начать", font_medium, YELLOW, 100)
        
        pygame.display.update()
        clock.tick(15)

# --- Основной цикл игры ---
def game_loop():
    # Вызываем стартовый экран перед началом
    game_intro()

    game_over = False
    game_close = False

    # Позиция игрока
    x = (DISPLAY_WIDTH * 0.45)
    y = (DISPLAY_HEIGHT * 0.75)
    x_change = 0
    player_speed = 8 # Скорость перемещения игрока влево/вправо

    # Параметры препятствий
    obs_startx = random.randrange(50, DISPLAY_WIDTH - CAR_WIDTH - 50)
    obs_starty = -600
    obs_speed = 7
    # Выбираем случайную картинку врага
    current_obs_img = random.choice(enemy_images)

    # Параметры фона (для скроллинга)
    bgY1 = 0
    bgY2 = -DISPLAY_HEIGHT

    score = 0

    while not game_over:

        while game_close:
            # Экран проигрыша
            pygame.draw.rect(game_display, BLACK, [DISPLAY_WIDTH/4, DISPLAY_HEIGHT/4, DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2])
            pygame.draw.rect(game_display, RED, [DISPLAY_WIDTH/4, DISPLAY_HEIGHT/4, DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2], 5)
            message_display("ВРЕЗАЛСЯ!", font_large, RED, -50)
            message_display(f"Ваш счет: {score}", font_medium, WHITE, 10)
            message_display("С - играть снова, Q - выход", font_small, YELLOW, 70)
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop() # Рестарт

        # Обработка управления
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -player_speed
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = player_speed
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        # Обновление позиции игрока
        x += x_change
        
        # Ограничение движения по краям дороги (небольшой отступ от края экрана)
        if x < 50: x = 50
        if x > DISPLAY_WIDTH - CAR_WIDTH - 50: x = DISPLAY_WIDTH - CAR_WIDTH - 50

        # --- ОТРИСОВКА ---

        # 1. Скроллинг фона
        # Двигаем две копии фона вниз
        bgY1 += obs_speed
        bgY2 += obs_speed

        # Если картинка ушла вниз, переносим её наверх
        if bgY1 >= DISPLAY_HEIGHT:
            bgY1 = -DISPLAY_HEIGHT
        if bgY2 >= DISPLAY_HEIGHT:
            bgY2 = -DISPLAY_HEIGHT
            
        # Рисуем две картинки фона друг над другом
        game_display.blit(bg_img, (0, bgY1))
        game_display.blit(bg_img, (0, bgY2))


        # 2. Движение и отрисовка врага
        obs_starty += obs_speed
        # Рисуем картинку врага
        game_display.blit(current_obs_img, (obs_startx, obs_starty))

        # 3. Отрисовка игрока
        game_display.blit(player_img, (x, y))

        # 4. Интерфейс
        show_score(score)
        show_speed(obs_speed)

        # --- ЛОГИКА ---

        # Если враг проехал мимо
        if obs_starty > DISPLAY_HEIGHT:
            obs_starty = 0 - CAR_HEIGHT - random.randint(100, 300) # Появляется с задержкой
            obs_startx = random.randrange(50, DISPLAY_WIDTH - CAR_WIDTH - 50)
            score += 1
            obs_speed += 0.3 # Увеличиваем скорость
            current_obs_img = random.choice(enemy_images) # Меняем скин врага

        # Проверка столкновений (Коллизия с использованием Rect)
        # Создаем невидимые прямоугольники вокруг машин для точной проверки
        player_rect = pygame.Rect(x, y, CAR_WIDTH, CAR_HEIGHT)
        enemy_rect = pygame.Rect(obs_startx, obs_starty, CAR_WIDTH, CAR_HEIGHT)

        # Функция colliderect проверяет пересечение
        if player_rect.colliderect(enemy_rect):
             # Небольшая задержка перед экраном проигрыша, чтобы увидеть аварию
            pygame.display.update()
            time.sleep(1)
            game_close = True

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

# Запуск
if __name__ == "__main__":
    game_loop()