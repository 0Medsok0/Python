import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Определение размеров окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Рыцарь против Скелетов")

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)  # Цвет платформ

# Загрузка и изменение размера изображений
knight_left_images = [pygame.image.load(f'sprites/mag_{i}.png') for i in range(1, 4)]
knight_right_images = [pygame.transform.flip(img, True, False) for img in knight_left_images]
skeleton_images_right = [pygame.image.load(f'sprites/skeleton_{i}.png') for i in range(1, 10)]
skeleton_images_left = [pygame.transform.flip(img, True, False) for img in skeleton_images_right]

strong_enemy_image_left = [pygame.image.load(f'sprites/dragon_{i}.png') for i in range(1, 4)]
strong_enemy_image_right = [pygame.transform.flip(img, True, False) for img in strong_enemy_image_left]

fireball_image = pygame.image.load('image/fireball.png')
fireball_image_left = pygame.transform.flip(fireball_image, True, False)
treasure_image = pygame.image.load('image/treasure.png')
background_image = pygame.image.load('image/bak.jpg')
platform_image = pygame.image.load('image/platform.png')

# Уменьшение изображений
knight_width, knight_height = 50, 50
skeleton_width, skeleton_height = 50, 50
fireball_width, fireball_height = 35, 35 # 35 35
strong_enemy_width, strong_enemy_height = 80, 80 # 60 60
treasure_width, treasure_height = 50, 50
platform_width, platform_height = 200, 20  # Размеры платформы
knight_right_images = [pygame.transform.scale(img, (knight_width, knight_height)) for img in knight_right_images]
knight_left_images = [pygame.transform.scale(img, (knight_width, knight_height)) for img in knight_left_images]
skeleton_images_right = [pygame.transform.scale(img, (skeleton_width, skeleton_height)) for img in skeleton_images_right]
skeleton_images_left = [pygame.transform.scale(img, (skeleton_width, skeleton_height)) for img in skeleton_images_left]
fireball_image = pygame.transform.scale(fireball_image, (fireball_width, fireball_height))
fireball_image_left = pygame.transform.scale(fireball_image_left, (fireball_width, fireball_height))
strong_enemy_image_right = [pygame.transform.scale(img, (strong_enemy_width, strong_enemy_height)) for img in strong_enemy_image_right]
strong_enemy_image_left = [pygame.transform.scale(img, (strong_enemy_width, strong_enemy_height)) for img in strong_enemy_image_left]
treasure_image = pygame.transform.scale(treasure_image, (treasure_width, treasure_height))
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
platform_image = pygame.transform.scale(platform_image, (platform_width, platform_height))

# Загрузка музыки
pygame.mixer.music.load('music/music.mp3')  # Добавьте музыку
pygame.mixer.music.play(-1)  # Воспроизведение музыки в бесконечном цикле

# Определение начальных параметров игры
knight_x = screen_width // 2
knight_y = screen_height - knight_height - 10
knight_speed = 5
skeleton_speed = 1
strong_enemy_speed = 2
knight_lives = 3
score = 0
level = 1
skeletons = []
strong_enemies = []
fireballs = []
treasures = []

# Параметры прыжка
jump_count = 0
jump_speed = 10
gravity = 0.5
is_jumping = False
fall_speed = 0

# Платформы
platforms = [
    pygame.Rect(100, 500, platform_width, platform_height),
    pygame.Rect(400, 400, platform_width, platform_height),
    pygame.Rect(600, 300, platform_width, platform_height)
]

# Функция для отображения текста
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Функция для отображения начального экрана
def start_screen():
    start_time = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    return start_time

        screen.blit(background_image, (0, 0))
        draw_text("Нажмите 'Старт' для начала игры", font, white, screen, screen_width // 2 - 200, screen_height // 2 - 50)
        pygame.draw.rect(screen, white, start_button_rect, border_radius=+10)
        draw_text("Старт", font, black, screen, start_button_rect.x + 20, start_button_rect.y + 10)
        pygame.display.flip()
        clock.tick(60)

# Функция для отображения конечного экрана
def end_screen(score, elapsed_time):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(background_image, (0, 0))
        draw_text(f"Игра окончена! Ваш счет: {score}", font, black, screen, screen_width // 2 - 150, screen_height // 2 - 50)
        draw_text(f"Время: {elapsed_time:.2f} секунд", font, black, screen, screen_width // 2 - 150, screen_height // 2)
        pygame.display.flip()
        clock.tick(60)

# Основной игровой цикл
running = True
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Направление движения рыцаря
knight_direction = 'right'
knight_animation_index = 0
knight_animation_timer = 0

# Параметры главного босса
boss_image = pygame.image.load('image/boss.png')
boss_width, boss_height = 100, 100
boss_image = pygame.transform.scale(boss_image, (boss_width, boss_height))
boss_x = screen_width - boss_width - 10 # справа появится
boss_y = screen_height - boss_height - 10
boss_lives = 10
boss_speed = 1

# Начальный экран
start_button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2, 100, 50)
start_time = start_screen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # Клавиша F для супер атаки
                fireballs.append([knight_x + knight_width // 2, knight_y + knight_height // 2, knight_direction])

    # Управление рыцарем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and knight_x > 0:
        knight_x -= knight_speed
        knight_direction = 'left'
    if keys[pygame.K_RIGHT] and knight_x < screen_width - knight_width:
        knight_x += knight_speed
        knight_direction = 'right'
    if keys[pygame.K_SPACE] and jump_count < 2:
        is_jumping = True
        jump_count += 1
        fall_speed = -jump_speed

    # Гравитация и прыжок
    if is_jumping:
        knight_y += fall_speed
        fall_speed += gravity
        if fall_speed > 0 and jump_count < 2:
            jump_count += 1
    else:
        knight_y += fall_speed
        fall_speed += gravity

    # Проверка столкновений с платформами и землей
    knight_rect = pygame.Rect(knight_x, knight_y, knight_width, knight_height)
    on_ground = False
    for platform in platforms:
        if knight_rect.colliderect(platform) and knight_y + knight_height <= platform.y + platform.height:
            knight_y = platform.y - knight_height
            fall_speed = 0
            jump_count = 0
            is_jumping = False
            on_ground = True
    if knight_y + knight_height >= screen_height:
        knight_y = screen_height - knight_height
        fall_speed = 0
        jump_count = 0
        is_jumping = False
        on_ground = True

    # Создание новых скелетов
    if level == 1 and random.randint(1, 200) < 5 and len(skeletons) < 5:
        side = random.choice(['left', 'right'])
        if side == 'left':
            skeletons.append([-skeleton_width, screen_height - skeleton_height - 10, 'right', 0, 0])
        else:
            skeletons.append([screen_width, screen_height - skeleton_height - 10, 'left', 0, 0])

    # Создание новых сильных врагов на втором уровне
    if level == 2 and random.randint(1, 400) < 5 and len(strong_enemies) < 2:
        side = random.choice(['left', 'right'])
        if side == 'left':
            strong_enemies.append([-strong_enemy_width, screen_height - strong_enemy_height - 10, 'right', 2, 0, 0])
        else:
            strong_enemies.append([screen_width, screen_height - strong_enemy_height - 10, 'left', 2, 0, 0])

    # Создание сокровищницы на втором уровне
    if level == 2 and len(treasures) == 0:
        treasures.append([random.randint(0, screen_width - treasure_width), screen_height - treasure_height - 10])

    # Создание сильных врагов на третьем уровне
    if level == 3 and random.randint(1, 400) < 5 and len(strong_enemies) < 5 and len(treasures) == 0:
        side = random.choice(['left', 'right'])
        if side == 'left':
            strong_enemies.append([-strong_enemy_width, screen_height - strong_enemy_height - 10, 'right', 2, 0, 0])
        else:
            strong_enemies.append([screen_width, screen_height - strong_enemy_height - 10, 'left', 2, 0, 0])
            treasures.append([random.randint(0, screen_width - treasure_width), screen_height - treasure_height - 10])


     # Перемещение скелетов и проверка столкновений
    for i in range(len(skeletons) - 1, -1, -1):
        skeleton = skeletons[i]
        if skeleton[2] == 'right':
            skeleton[0] += skeleton_speed
        else:
            skeleton[0] -= skeleton_speed

        # Проверка столкновения с рыцарем
        if (skeleton[0] < knight_x + knight_width and skeleton[0] + skeleton_width > knight_x and
            skeleton[1] < knight_y + knight_height and skeleton[1] + skeleton_height > knight_y):
            skeletons.pop(i)
            knight_lives -= 1
            if knight_lives <= 0:
                running = False

        # Проверка выхода за пределы экрана
        if skeleton[0] > screen_width or skeleton[0] + skeleton_width < 0:
            skeletons.pop(i)

        # Обновление анимации скелета
        skeleton[4] += 1
        if skeleton[4] >= 10:  # Скорость анимации
            skeleton[4] = 0
            skeleton[3] = (skeleton[3] + 1) % len(skeleton_images_left)

    # Перемещение сильных врагов и проверка столкновений
    for i in range(len(strong_enemies) - 1, -1, -1):
        strong_enemy = strong_enemies[i]
        if strong_enemy[2] == 'right':
            strong_enemy[0] += strong_enemy_speed
        else:
            strong_enemy[0] -= strong_enemy_speed

        # Проверка столкновения с рыцарем
        if (strong_enemy[0] < knight_x + knight_width and strong_enemy[0] + strong_enemy_width > knight_x and
            strong_enemy[1] < knight_y + knight_height and strong_enemy[1] + strong_enemy_height > knight_y):
            strong_enemy[3] -= 1
            if strong_enemy[3] <= 0:
                strong_enemies.pop(i)
                score += 20
            knight_lives -= 1
            if knight_lives <= 0:
                running = False

        # Проверка выхода за пределы экрана
        if strong_enemy[0] > screen_width or strong_enemy[0] + strong_enemy_width < 0:
            strong_enemies.pop(i)

        strong_enemy[5] += 1
        if strong_enemy[5] >= 10:  # Скорость анимации
            strong_enemy[5] = 0
            strong_enemy[4] = (strong_enemy[4] + 1) % len(strong_enemy_image_right)

    # Перемещение огненных шаров и проверка столкновений
    for i in range(len(fireballs) - 1, -1, -1):
        fireball = fireballs[i]
        if fireball[2] == 'right':
            fireball[0] += 10
        else:
            fireball[0] -= 10

        # Проверка столкновения с скелетами
        for j in range(len(skeletons) - 1, -1, -1):
            skeleton = skeletons[j]
            if (fireball[0] < skeleton[0] + skeleton_width and fireball[0] + fireball_width > skeleton[0] and
                fireball[1] < skeleton[1] + skeleton_height and fireball[1] + fireball_height > skeleton[1]):
                skeletons.pop(j)
                fireballs.pop(i)
                score += 10
                break

        # Проверка столкновения с сильными врагами
        for j in range(len(strong_enemies) - 1, -1, -1):
            strong_enemy = strong_enemies[j]
            if (fireball[0] < strong_enemy[0] + strong_enemy_width and fireball[0] + fireball_width > strong_enemy[0] and
                fireball[1] < strong_enemy[1] + strong_enemy_height and fireball[1] + fireball_height > strong_enemy[1]):
                strong_enemy[3] -= 1
                if strong_enemy[3] <= 0:
                    strong_enemies.pop(j)
                    score += 20
                fireballs.pop(i)
                break

        # Проверка выхода за пределы экрана
        if fireball[0] > screen_width or fireball[0] + fireball_width < 0:
            fireballs.pop(i)

    # Проверка столкновения с сокровищницей
    for i in range(len(treasures) - 1, -1, -1):
        treasure = treasures[i]
        if (knight_x < treasure[0] + treasure_width and knight_x + knight_width > treasure[0] and
            knight_y < treasure[1] + treasure_height and knight_y + knight_height > treasure[1]):
            treasures.pop(i)
            score += 250

    # Переход на следующий уровень
    if score >= 500 and level == 1:
        level = 2
        skeletons = []
        strong_enemies = []
        fireballs = []
        treasures = []
        knight_x = screen_width // 2
        knight_y = screen_height - knight_height - 10
    elif score >= 2000 and level == 2:
        level = 3
        skeletons = []
        strong_enemies = []
        fireballs = []
        treasures = []
        knight_x = screen_width // 2
        knight_y = screen_height - knight_height - 10
    elif score >= 4000 and level == 3:
        level = 4
        skeletons = []
        strong_enemies = []
        fireballs = []
        treasures = []
        knight_x = screen_width // 2
        knight_y = screen_height - knight_height - 10


    # Логика для главного босса на 4 уровне
    boss_direction = 'left'  # Начальное направление босса
    if level == 4:
        if knight_x < boss_x:
            boss_x -= boss_speed
            boss_direction = 'left'
        else:
            boss_x += boss_speed
            boss_direction = 'right'


        # Проверка столкновения с рыцарем
        if (boss_x < knight_x + knight_width and boss_x + boss_width > knight_x and
            boss_y < knight_y + knight_height and boss_y + boss_height > knight_y):
            knight_lives -= 1
            if knight_lives <= 0:
                running = False

        # Проверка столкновения с огненными шарами
        for i in range(len(fireballs) - 1, -1, -1):
            fireball = fireballs[i]
            if (fireball[0] < boss_x + boss_width and fireball[0] + fireball_width > boss_x and
                fireball[1] < boss_y + boss_height and fireball[1] + fireball_height > boss_y):
                boss_lives -= 1
                fireballs.pop(i)
                if boss_lives <= 0:
                    running = False  # Игра заканчивается, когда босс повержен

    # Очистка экрана
    screen.blit(background_image, (0, 0))

    # Анимация рыцаря
    knight_animation_timer += 1
    if knight_animation_timer >= 10:  # Скорость анимации
        knight_animation_timer = 0
        knight_animation_index = (knight_animation_index + 1) % len(knight_right_images)

    # Отображение рыцаря
    if knight_direction == 'right':
        screen.blit(knight_right_images[knight_animation_index], (knight_x, knight_y))
    else:
        screen.blit(knight_left_images[knight_animation_index], (knight_x, knight_y))

    # Отображение скелетов
    for skeleton in skeletons:
        if skeleton[2] == 'right':
            screen.blit(skeleton_images_right[skeleton[3]], (skeleton[0], skeleton[1]))
        else:
            screen.blit(skeleton_images_left[skeleton[3]], (skeleton[0], skeleton[1]))

    # Отображение сильных врагов
    for strong_enemy in strong_enemies:
        if strong_enemy[2] == 'right':
            screen.blit(strong_enemy_image_left[strong_enemy[4]], (strong_enemy[0], strong_enemy[1]))
        else:
            screen.blit(strong_enemy_image_right[strong_enemy[4]], (strong_enemy[0], strong_enemy[1]))

    # Отображение огненных шаров
    for fireball in fireballs:
        if fireball[2] == 'right':
            screen.blit(fireball_image, (fireball[0], fireball[1]))
        else:
            screen.blit(fireball_image_left, (fireball[0], fireball[1]))

    # Отображение сокровищницы
    for treasure in treasures:
        screen.blit(treasure_image, (treasure[0], treasure[1]))

    # Отображение платформ
    for platform in platforms:
        screen.blit(platform_image, (platform.x, platform.y))

    # Отображение счета и жизней
    draw_text(f"Счет: {score}", font, black, screen, 10, 10)
    draw_text(f"Жизни: {knight_lives}", font, black, screen, 10, 40)
    draw_text(f"Уровень: {level}", font, black, screen, 10, 70)

    # Отображение главного босса на 4 уровне
    if level == 4:
        screen.blit(boss_image, (boss_x, boss_y))
        draw_text(f"Жизни босса: {boss_lives}", font, black, screen, 10, 100)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

# Конечный экран
elapsed_time = time.time() - start_time
end_screen(score, elapsed_time)

# Завершение игры
pygame.quit()
