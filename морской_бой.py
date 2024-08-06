import random

def create_field():
  """Создает игровое поле 10x10."""
  field = [[' ' for _ in range(10)] for _ in range(10)]
  return field

def print_field(field):
  """Выводит игровое поле на экран."""
  print("   1 2 3 4 5 6 7 8 9 10")
  for i, row in enumerate(field):
    print(f"{i + 1}  {' '.join(row)}")

def place_ship(field, ship_size):
  """Размещает корабль на поле."""
  while True:
    horizontal = random.choice([True, False])
    if horizontal:
      x = random.randint(0, 10 - ship_size)
      y = random.randint(0, 9)
    else:
      x = random.randint(0, 9)
      y = random.randint(0, 10 - ship_size)
    if all(
        0 <= x + i * (1 if horizontal else 0) <= 9
        and 0 <= y + i * (1 if not horizontal else 0) <= 9
        and field[y + i * (1 if not horizontal else 0)][x + i * (1 if horizontal else 0)] == ' '
        for i in range(ship_size)
    ):
      for i in range(ship_size):
        field[y + i * (1 if not horizontal else 0)][x + i * (1 if horizontal else 0)] = '■'
      return

def generate_ships(field):
  """Генерирует корабли на поле."""
  ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
  for ship_size in ships:
    place_ship(field, ship_size)

def player_turn(player_field, enemy_field):
  """Ход игрока."""
  while True:
    try:
      x, y = map(int, input(f"Введите координаты выстрела (x y): ").split())
      if not (1 <= x <= 10 and 1 <= y <= 10):
        print("Некорректные координаты.")
      elif enemy_field[y - 1][x - 1] == '■':
        enemy_field[y - 1][x - 1] = 'X'
        print("Попадание!")
        return True
      elif enemy_field[y - 1][x - 1] == ' ':
        enemy_field[y - 1][x - 1] = 'O'
        print("Промах.")
        return False
      else:
        print("Вы уже стреляли в эту клетку.")
    except (ValueError, IndexError):
      print("Некорректный ввод.")

def check_win(field):
  """Проверяет, победил ли игрок."""
  for row in field:
    for cell in row:
      if cell == '■':
        return False
  return True

def main():
  """Основная функция."""
  player_field = create_field()
  enemy_field = create_field()

  generate_ships(player_field)
  generate_ships(enemy_field)

  print("Ваше поле:")
  print_field(player_field)

  print("\nПоле противника:")
  print_field(enemy_field)

  while True:
    print("\nВаш ход:")
    if player_turn(player_field, enemy_field):
      print("\nПоле противника:")
      print_field(enemy_field)
      if check_win(enemy_field):
        print("\nВы победили!")
        break
    else:
      print("\nХод противника:")
      print_field(enemy_field)
      if player_turn(enemy_field, player_field):
        print("\nВы проиграли!")
        break

if __name__ == "__main__":
  main()
