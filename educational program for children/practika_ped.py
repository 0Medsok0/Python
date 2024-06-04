import random
from test_matpotlib import plot_isosceles_triangle,equilateral_triangle,an_obtuse_triangle,Square,rectangle,Trapezoid,circle,Oval
import time

def show_menu():
  print("----- Меню -----")
  print("1. Выбор класса")
  print("2. Пройти тест")
  print("3. Просмотреть результаты")
  print("4. Выход")

def choose_class():
  print("----- Выбор класса -----")
  print("1. 1 класс")
  print("2. 2 класс")
  print("3. 3 класс")
  print("4. 4 класс")

  while True:
    class_choice = input("Введите номер класса: ")
    if class_choice in ['1', '2', '3', '4']:
      return int(class_choice)
    else:
      print("Некорректный ввод. Пожалуйста, введите число от 1 до 4.")

def choose_topic(class_choice):
  topics = {
    1: ["Сложение в пределах 10", "Вычитание в пределах 10"],
    2: ["Сложение в пределах 20", "Вычитание в пределах 20"],
    3: ["Таблица умножения", "Деление на 2, 3, 4, 5, 10"],
    4: ["Геометрические фигуры", "Периметр и площадь"]
  }

  print(f"----- Темы для {class_choice} класса -----")
  for i, topic in enumerate(topics[class_choice], 1):
    print(f"{i}. {topic}")

  while True:
    topic_choice = input("Введите номер темы: ")
    if topic_choice in [str(i) for i in range(1, len(topics[class_choice]) + 1)]:
      return topics[class_choice][int(topic_choice) - 1]
    else:
      print("Некорректный ввод. Пожалуйста, введите число из списка.")

# Отвечает за обучение
def start_learning(topic):
  print(f"----- Обучение теме: {topic} -----")
  if topic == "Сложение в пределах 10":
    addition_10()
  if topic == "Вычитание в пределах 10":
    subtraction_10()
  if topic == 'Сложение в пределах 20':
    addition_20()
  if topic == "Вычитание в пределах 20":
    subtraction_20()
  if topic == 'Таблица умножения':
    multiplication_table()
  if topic == "Деление на 2, 3, 4, 5, 10":
    division_by_numbers()
  if topic == 'Геометрические фигуры':
    geometric_shapes()
  if topic == "Периметр и площадь":
    perimeter_and_area()

  # ... (добавить логику обучения для других тем)
  
  
# Отвечает за тесты
def start_test(topic):
  print(f"----- Тест по теме: {topic} -----")
  
  if topic == "Сложение в пределах 10":
    addition_10_test()
  elif topic == "Вычитание в пределах 10":
    subtraction_10_test()
  elif topic == "Сложение в пределах 20":
    addition_20_test()
  elif topic == "Вычитание в пределах 20":
    subtraction_20_test()
  elif topic == "Таблица умножения":
    multiplication_test()
  elif topic == "Деление на 2, 3, 4, 5, 10":
    division_test()
  elif topic == "Геометрические фигуры":
    geometric_shapes_test()
  elif topic == "Периметр и площадь":
    perimeter_and_area_test()


test_results = []
def track_progress():
    print("----- Результаты -----")
    if test_results:
        for result in test_results:
            print(f"Имя: {result[0]}, Баллы: {result[1]}, Время: {result[2]}")
    else:
        print("Результаты тестов отсутствуют.")


# 1 Класс (2 Темы 2 теста)
def addition_10():
  num1 = random.randint(1, 9)
  num2 = random.randint(1, 9)
  
  text = [
          'Сложение чисел от 1 до 10 - это очень просто! Давай считать вместе.',
          '1 + 2 = 3',
          '3 + 3 = 6',
          '4 + 5 = 9',
          '6 + 4 = 10',
          '7 + 3 = 10',
          '8 + 2 = 10',
          'Теперь давай попробуем сложить все числа от 1 до 10. Для этого начнем с 1 и будем прибавлять по одному числу, пока не дойдем до 10.',
          '1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55',
          'Вот и всё! Теперь ты знаешь, как складывать числа от 1 до 10.'
          ]
  for i in text:
    print(i, end='\n')

  print(f"\n Сколько будет {num1} + {num2}?")
  user_answer = int(input("Введите ответ: "))

  if user_answer == num1 + num2:
    print("Правильно!")
  else:
    print(f"Неверно. Правильный ответ: {num1 + num2}")

def subtraction_10():
  num1 = random.randint(1, 9)
  num2 = random.randint(1, num1)
  
  text = [
          'Вычитание чисел от 1 до 10 — это тоже очень просто! Давай считать вместе.',
          '10 – 1 = 9,',
          '9 – 3 = 6,',
          '6 – 4 = 2,',
          '2 – 5 = –3,',
          '–3 – 6 = –9,',
          '–9 – 7 = –16,',
          '–16 – 8 = –24,',
          '–24 – 9 = –33,',
          '–33 – 10 = –43.',
          'Вот и всё! Теперь ты знаешь, как вычитать числа от 10 до 1.'
          ]
  for i in text:
    print(i, end='\n')

  print(f"\n Сколько будет {num1} + {num2}?")
  user_answer = int(input("Введите ответ: "))

  print(f"Сколько будет {num1} - {num2}?")
  user_answer = int(input("Введите ответ: "))

  if user_answer == num1 - num2:
    print("Правильно!")
  else:
    print(f"Неверно. Правильный ответ: {num1 - num2}")

def addition_10_test():
  score = 0
  start_time = time.time()
  for _ in range(5):
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    print(f"Сколько будет {num1} + {num2}?")
    user_answer = int(input("Введите ответ: "))

    if user_answer == num1 + num2:
      print("Правильно!")
      score += 1
    else:
      print(f"Неверно. Правильный ответ: {num1 + num2}")
  
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Ваш результат: {score} из 5")
  name = input("Введите ваше имя: ")
  test_results.append((name, score, elapsed_time))

def subtraction_10_test():
  score = 0
  start_time = time.time()
  for _ in range(5):
    num1 = random.randint(1, 9)
    num2 = random.randint(1, num1)

    print(f"Сколько будет {num1} - {num2}?")
    user_answer = int(input("Введите ответ: "))

    if user_answer == num1 - num2:
      print("Правильно!")
      score += 1
    else:
      print(f"Неверно. Правильный ответ: {num1 - num2}")
  
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Ваш результат: {score} из 5")
  name = input("Введите ваше имя: ")
  test_results.append((name, score, elapsed_time))

# 2 Класс (2 Темы 2 Теста)
def addition_20():
  num1 = random.randint(1, 9)
  num2 = random.randint(1, 9)
  
  text = [
        'Сложение чисел от 1 до 20 — это тоже очень просто! Давай считать вместе.',
        '1 + 2 = 3.',
        '3 + 3 = 6.',
        '4 + 5 = 9.',
        '6 + 4 = 10.',
        '7 + 3 = 10.',
        '8 + 2 = 10.',
        'Теперь давай попробуем сложить все числа от 1 до 20. Для этого начнём с 1 и будем прибавлять по одному числу, пока не дойдём до 20.',
        '1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20 = 210.',
        'Вот и всё! Теперь ты знаешь, как складывать числа от 1 до 20.'
        ]
  for i in text:
    print(i, end='\n')
  
  print(f"Сколько будет {num1} + {num2}?")
  user_answer = int(input("Введите ответ: "))

  if user_answer == num1 + num2:
    print("Правильно!")
  else:
    print(f"Неверно. Правильный ответ: {num1 + num2}")
    
def subtraction_20():
  num1 = random.randint(1, 19)
  num2 = random.randint(1, num1)
  
  text = [
    'Вычитание чисел от 1 до 20 — это тоже очень просто! Давай считать вместе.',
    '20 - 1 = 19.',
    '19 - 2 = 17.',
    '17 - 3 = 14.',
    '14 - 4 = 10.',
    '10 - 5 = 5.',
    '5 - 6 = -1.',
    'Теперь давай попробуем вычесть все числа от 1 до 20 из числа 20. Для этого начнём с 20 и будем вычитать по одному числу, пока не дойдём до 1.',
    '20 - 1 = 19.',
    '19 - 2 = 17.',
    '17 - 3 = 14.',
    '14 - 4 = 10.',
    '10 - 5 = 5.',
    '5 - 6 = -1.',
    'Вот и всё! Теперь ты знаешь, как вычитать числа от 1 до 20 из числа 20.'
  ]
  for i in text:
    print(i, end='\n')

  print(f"Сколько будет {num1} - {num2}?")
  user_answer = int(input("Введите ответ: "))

  if user_answer == num1 - num2:
    print("Правильно!")
  else:
    print(f"Неверно. Правильный ответ: {num1 - num2}")

def addition_20_test():
  score = 0
  start_time = time.time()
  for _ in range(5):
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 11)

    print(f"Сколько будет {num1} + {num2}?")
    user_answer = int(input("Введите ответ: "))

    if user_answer == num1 + num2:
      print("Правильно!")
      score += 1
    else:
      print(f"Неверно. Правильный ответ: {num1 + num2}")

  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Ваш результат: {score} из 5")
  name = input("Введите ваше имя: ")
  test_results.append((name, score, elapsed_time))

def subtraction_20_test():
  score = 0
  start_time = time.time()
  for _ in range(5):
    num1 = random.randint(1, 19)
    num2 = random.randint(1, num1)

    print(f"Сколько будет {num1} - {num2}?")
    user_answer = int(input("Введите ответ: "))

    if user_answer == num1 - num2:
      print("Правильно!")
      score += 1
    else:
      print(f"Неверно. Правильный ответ: {num1 - num2}")

  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Ваш результат: {score} из 5")
  name = input("Введите ваше имя: ")
  test_results.append((name, score, elapsed_time))


# 3 Класс (2 Темы 2 Теста)
def multiplication_table():
  print('Дорогой ученик, перед тобой таблица умножения', end='\n')
  print('--------------------------------------', end='\n')
  for i in range(2,10):
    for j in range(1,11):
      print(i, '*', j, '=', i*j,end='\n')
    if i == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
      print('--------------------------------------', end='\n')

def division_by_numbers():
  """
  Функция делит число, введенное пользователем, на 2, 3, 4, 5, 10, если это возможно, и выводит результат.
  """
  print('Введите число для проверки на делимость 2, 3, 4, 5, 10', end='\n')
  divisors = [2, 3, 4, 5, 10]
  number = int(input("Введите число: "))

  for divisor in divisors:
    if number % divisor == 0:
      result = number // divisor
      print(f"{number} делится на {divisor} без остатка, результат: {result}")

def multiplication_test():
  """
  Функция проводит короткий тест по таблице умножения.
  """
  score = 0
  start_time = time.time()
  questions = [
    (random.randint(2, 9), random.randint(1, 10)),
    (random.randint(2, 9), random.randint(1, 10)),
    (random.randint(2, 9), random.randint(1, 10)),
    (random.randint(2, 9), random.randint(1, 10)),
    (random.randint(2, 9), random.randint(1, 10))
  ]
  for num1, num2 in questions:
    print(f"Сколько будет {num1} * {num2}?")
    user_answer = int(input("Введите ответ: "))
    if user_answer == num1 * num2:
      print("Правильно!")
      score += 1
    else:
      print(f"Неверно. Правильный ответ: {num1 * num2}")

  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Ваш результат: {score} из 5")
  name = input("Введите ваше имя: ")
  test_results.append((name, score, elapsed_time))

def division_test():
  """
  Функция проводит короткий тест по делению на 2, 3, 4, 5, 10.
  """
  score = 0
  start_time = time.time()
  questions = [
    (random.randint(2, 50), random.choice([2, 3, 4, 5, 10])),
    (random.randint(2, 50), random.choice([2, 3, 4, 5, 10])),
    (random.randint(2, 50), random.choice([2, 3, 4, 5, 10])),
    (random.randint(2, 50), random.choice([2, 3, 4, 5, 10])),
    (random.randint(2, 50), random.choice([2, 3, 4, 5, 10]))
  ]
  for num, divisor in questions:
    print(f"Сколько будет {num} / {divisor}?")
    user_answer = int(input("Введите ответ: "))
    if user_answer == num // divisor:
      print("Правильно!")
      score += 1
    else:
      print(f"Неверно. Правильный ответ: {num // divisor}")
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Ваш результат: {score} из 5")
  name = input("Введите ваше имя: ")
  test_results.append((name, score, elapsed_time))
  

# 4 Класс (2 Темы 2 Теста)
def geometric_shapes():
    print('Дорогой ученик, предлагаем тебе изучить геометрические фигуры ','выбери нужный пункт меню и начни изучать геометрические фигуры', end='\n')
    print('Введите начальное число от 1 до 10')
    question = 0
    question += int(input('\n 1 -- Равнобедренный треугольник \n 2 -- Равносторонний треугольник \n 3 -- Тупоугольный треугольник \
    \n 4 -- Квадрат \n 5 -- Прямоугольник \
    \n 6 -- Трапеция \n 7 -- Круг \
    \n 8 -- Овал \n'))
    
    if question == 1:
      text = ['Равнобедренный треугольник – это треугольник, у которого две стороны равны. Эти равные стороны называются боковыми, а третья сторона – основанием. У равнобедренного треугольника есть одна ось симметрии, проходящая через вершинный угол и середину основания.',
              'Свойства равнобедренного треугольника включают равенство углов при основании, равенство биссектрис, медиан и высот, проведенных из углов при основании. Также совпадают между собой биссектриса, медиана, высота и серединный перпендикуляр, проведенные к основанию.',
              'Площадь равнобедренного треугольника можно найти несколькими способами, например, как половину произведения основания на высоту или как половину квадрата боковой стороны, умноженную на синус угла при основании.',
              'Равнобедренный треугольник имеет важное значение в геометрии и математике, так как его свойства используются для решения различных задач и доказательств теорем.']
      for i in text:
        print(i, end='\n')
      time.sleep(3)
      print(f'\n\n Сейчас откроется фигура равнобедренного треугольника для ознакомления')
      plot_isosceles_triangle()
      
    elif question == 2: 
      text = ['Равносторонний треугольник — это особый вид треугольников, у которого все три стороны равны между собой. Также равны и углы такого треугольника. Каждый угол при вершине равностороннего треугольника равен 60 градусам.']
      for i in text:
        print(i, end='\n')
      time.sleep(3)
      print(f'\n\n Сейчас откроется фигура равностороннего треугольника для ознакомления')
      equilateral_triangle()
      
    elif question == 3:
      text = ['Тупоугольный треугольник — это треугольник, у которого один из углов больше 90 градусов, но меньше 180 градусов. Два других угла этого треугольника всегда острые. Тупоугольный треугольник может быть разносторонним или равнобедренным. В равнобедренном тупоугольном треугольнике углы при основании равны, а угол между ними тупой.']
      for i in text:
        print(i, end='\n')
      time.sleep(3)
      print(f'\n\n Сейчас откроется фигура тупоугольного треугольника для ознакомления')
      an_obtuse_triangle()
      
    elif question == 4:
      text = ['Квадрат – это геометрическая фигура, которая является частным случаем прямоугольника, где все стороны равны. У квадрата четыре равные стороны и четыре прямых угла, каждый из которых равен 90°. Диагонали квадрата также равны и пересекаются под прямым углом, делясь пополам. Важной особенностью квадрата является то, что в него можно вписать окружность, радиус которой равен половине длины стороны квадрата, и описать вокруг него окружность, радиус которой равен половине длины диагонали квадрата.']
      for i in text:
        print(i, end='\n')
      time.sleep(3)
      print(f'\n\n Сейчас откроется фигура квадрата для ознакомления')
      Square()
      
    elif question == 5:
      text = ['Прямоугольник — это четырёхугольник, у которого все углы прямые, то есть равны 90°. Слово «прямоугольник» происходит от латинского rectangulus, что означает «прямой угол».',
              'В евклидовой геометрии для того, чтобы четырёхугольник был прямоугольником, достаточно, чтобы хотя бы три его угла были прямые. Тогда четвёртый угол в силу теоремы о сумме углов многоугольника также будет равен 90°.',
              'Противоположные стороны прямоугольника равны и параллельны. Диагонали прямоугольника также равны и делятся точкой пересечения пополам.',
              'Площадь прямоугольника равна произведению его длины на ширину. Периметр прямоугольника равен удвоенной сумме длин его ширины и длины.']
      for i in text:
        print(i, end='\n')
      time.sleep(3)
      print(f'\n\n Сейчас откроется фигура прямоугольника для ознакомления')
      rectangle(2,4)
      
    elif question == 6:
      text = ['Трапеция - это четырёхугольник, у которого две противоположные стороны параллельны, а две другие - не параллельны. Эти непараллельные стороны называются основаниями трапеции. Параллельные стороны могут быть как равными, так и неравными.',
              'Элементы трапеции:',
              'a и b - основания трапеции, где a || b;',
              'h - высота трапеции, расстояние между основаниями, h ⊥ a, b;',
              'm - средняя линия трапеции, отрезок, соединяющий середины боковых сторон.',
              'Свойства трапеции:',
              'Сумма углов, прилежащих к боковой стороне, равна 180°.',
              'Треугольники, образованные боковыми сторонами и основаниями, подобны.',
              'Виды трапеций:',
              'Прямоугольная трапеция - имеет прямые углы при одной из боковых сторон.',
              'Равнобедренная трапеция - боковые стороны равны.',
              'Произвольная трапеция - не относится ни к одному из предыдущих видов.',
              'Площадь трапеции:',
              'Через основания и высоту: S = (a + b) / 2 * h.',
              'Через среднюю линию и высоту: S = m * h.',
              'Через диагонали и угол между ними: S = 1/2 * d1 * d2 * sin(γ), где γ - угол между диагоналями.'
              ]
      for i in text:
        print(i, end='\n')
      time.sleep(3)
      print(f'\n\n Сейчас откроется фигура трапеции для ознакомления')
      Trapezoid(2,4)
      
    elif question == 7:
      text = ['Круг – это часть плоскости, ограниченная окружностью, где все точки находятся на одинаковом расстоянии от центра. Центр круга – это точка, равноудаленная от любой точки на его границе. Радиус круга – это отрезок, соединяющий центр с любой точкой на окружности. Диаметр – это отрезок, проходящий через центр и соединяющий две точки на окружности.',
              'Площадь круга вычисляется по формуле: (S = \pi R^2), где (R) – радиус круга, а (\pi) приблизительно равно 3.14159. Длина окружности (периметр круга) определяется как (L = 2 \pi R).'
              ]
      for i in text:
        print(i, end='\n')
      time.sleep(3)
      print(f'\n\n Сейчас откроется фигура круга для ознакомления')
      circle()
      
    elif question == 8:
      text = ['Овал - это плоская замкнутая строго выпуклая гладкая кривая, имеющая с любой прямой не более двух общих точек. Простейшим примером овала является эллипс, который можно рассматривать как частный случай овала.',
              'Основные свойства овала включают наличие вершин, в которых кривизна достигает экстремума, и теорему о четырех вершинах, утверждающую, что овал имеет не менее четырех вершин. Также, если овал имеет в каждой своей точке определенную касательную, то любому направлению на плоскости соответствуют две и только две касательные, параллельные этому направлению.',
              'В алгебраической геометрии овалом также называют просто замкнутые (не обязательно выпуклые) связные компоненты плоских алгебраических кривых. В черчении овал строится из двух пар дуг с разными радиусами и центрами, соединенных в точке, где касательные к обеим дугам лежат на одной прямой, обеспечивая гладкое соединение.',
              'Вариации овала включают овалы с двумя осями симметрии, построенные из четырех дуг, и различные формы, такие как овал Кассини и овал Декарта.',
              ]
      for i in text:
        print(i, end='\n')
      time.sleep(3)
      print(f'\n\n Сейчас откроется фигура овала для ознакомления')
      Oval()
    
def perimeter_and_area():
    text = ['Периметр – это сумма длин всех сторон фигуры. Чтобы найти периметр прямоугольника или квадрата, нужно сложить длины всех его сторон. Например, если у нас есть прямоугольник со сторонами 4 см и 5 см, то его периметр будет равен 4 см + 5 см + 4 см + 5 см = 18 см.',
            'Площадь – это количество места, которое занимает фигура на плоскости. Чтобы найти площадь прямоугольника, нужно умножить длину на ширину. Например, если у нас есть прямоугольник со сторонами 2 см и 5 см, то его площадь будет равна 2 см × 5 см = 10 см².',
            'Для квадрата, чтобы найти периметр, нужно умножить длину одной стороны на 4. Например, если сторона квадрата равна 3 см, то его периметр будет равен 3 см × 4 = 12 см. Чтобы найти площадь квадрата, нужно возвести длину стороны в квадрат. Например, если сторона квадрата равна 4 см, то его площадь будет равна 4 см² × 4 см² = 16 см².',
            'Важно помнить, что для нахождения периметра и площади фигуры нужно знать её размеры.']
    for i in text:
      print(i, end = '\n')

def geometric_shapes_test():
    questions = [
    {
        "question": "Какая геометрическая фигура имеет три стороны?",
        "answers": ["Треугольник", "Квадрат", "Круг"],
        "correct_answer": "Треугольник"
    },
    {
        "question": "Какая фигура имеет четыре прямых угла?",
        "answers": ["Прямоугольник", "Треугольник", "Овал"],
        "correct_answer": "Прямоугольник"
    },
    {
        "question": "Какая геометрическая фигура не имеет углов?",
        "answers": ["Круг", "Квадрат", "Треугольник"],
        "correct_answer": "Круг"
    }
  ]
    random.shuffle(questions)
    score = 0
    start_time = time.time()
    print("Тест по геометрическим фигурам")
    for i, question in enumerate(questions):
        print(f"\nВопрос {i + 1}: {question['question']}")
        random.shuffle(question['answers'])
        for j, answer in enumerate(question['answers']):
            print(f"{chr(ord('A') + j)}. {answer}")
        user_answer = input("Введите букву с номером правильного ответа: ").upper()
        if user_answer == chr(ord('A') + question['answers'].index(question['correct_answer'])):
            print("Правильно!")
            score += 1
        else:
            print(f"Неверно. Правильный ответ: {question['correct_answer']}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Ваш результат: {score} из 3")
    name = input("Введите ваше имя: ")
    test_results.append((name, score, elapsed_time))

def perimeter_and_area_test():
    questions = [
    {
        "question": "Периметр прямоугольника со сторонами 5 см и 3 см равен:",
        "answers": ["15 см", "8 см", "16 см"],
        "correct_answer": "16 см"
    },
    {
        "question": "Площадь квадрата со стороной 4 см равна:",
        "answers": ["16 см²", "8 см²", "12 см²"],
        "correct_answer": "16 см²"
    },
    {
        "question": "Периметр треугольника со сторонами 6 см, 8 см и 10 см равен:",
        "answers": ["24 см", "18 см", "20 см"],
        "correct_answer": "24 см"
    }
]
    random.shuffle(questions)
    score = 0
    start_time = time.time()
    print("Тест по периметру и площади")
    for i, question in enumerate(questions):
        print(f"\nВопрос {i + 1}: {question['question']}")
        random.shuffle(question['answers'])
        for j, answer in enumerate(question['answers']):
            print(f"{chr(ord('A') + j)}. {answer}")
        user_answer = input("Введите букву с номером правильного ответа: ").upper()
        if user_answer == chr(ord('A') + question['answers'].index(question['correct_answer'])):
            print("Правильно!")
            score += 1
        else:
            print(f"Неверно. Правильный ответ: {question['correct_answer']}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Ваш результат: {score} из 3")
    name = input("Введите ваше имя: ")
    test_results.append((name, score, elapsed_time))

    
while True:
  show_menu()
  choice = input("Введите номер пункта меню: ")

  if choice == '1':
    class_choice = choose_class()
    topic = choose_topic(class_choice)
    start_learning(topic)
  elif choice == '2':
    class_choice = choose_class()
    topic = choose_topic(class_choice)
    start_test(topic)
  elif choice == '3':
    track_progress()
  elif choice == '4':
    print("До свидания!")
    break
  else:
    print("Некорректный ввод. Пожалуйста, введите число от 1 до 4.")