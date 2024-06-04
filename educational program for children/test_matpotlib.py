import matplotlib.pyplot as plt
import numpy as np

# Равностронний треугольник
def equilateral_triangle():
    # Координаты вершин треугольника
    x = [0, 1, 0.5, 0]
    y = [0, 0, 1, 0]
    # Построение треугольника
    plt.plot(x, y,'r-')  # 'r-' - красный цвет, сплошная линия
    plt.xlabel('Ось X')  # Подпись оси X
    plt.ylabel('Ось Y')  # Подпись оси Y
    plt.title('Равностронний треугольник')  # Заголовок графика
    plt.grid(True)  # Включение сетки
    # Отображение графика
    plt.show()
# Равнобедренный треугольник
def plot_isosceles_triangle():
  """
  Строит равнобедренный треугольник с заданной основой и высотой.
  Args:
    base: Длина основания треугольника.
    height: Высота треугольника.
  """
  # Координаты вершин
  x = np.array([0, 2/2, 2, 0])
  y = np.array([0, 4, 0, 0])
  # Построение треугольника
  plt.plot(x, y, 'r-')
  # Настройка графика
  plt.xlabel('Ось X')
  plt.ylabel('Ось Y')
  plt.title('Равнобедренный треугольник')
  plt.xlim(-1, 2 + 1)  # Установка границ по оси X
  plt.ylim(-1, 4 + 1)  # Установка границ по оси Y
  plt.grid(True)  # Включение сетки
  plt.show()
# Тупоугольный треугольник
def an_obtuse_triangle():
    # Координаты вершин треугольника
    x = [0, 1, 0, 0]
    y = [0, 0, 1, 0]

    # Построение треугольника
    plt.plot(x, y,'b-')  # 'r-' - красный цвет, сплошная линия
    plt.xlabel('Ось X')  # Подпись оси X
    plt.ylabel('Ось Y')  # Подпись оси Y
    plt.title('Тупоугольный треугольник')  # Заголовок графика
    plt.grid(True)  # Включение сетки
    # Отображение графика
    plt.show()
# Квадрат
def Square():
    x = [] 
    y = []
    # Построение графика
    plt.show(x,y, 'r-')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.title('Квадрат')
    plt.grid(True)
    plt.show()
# Прямоугольник
def rectangle(base,height):
    x = np.array([0,base,base,0,0]) 
    y = np.array([2.65,height/1.5,0,0,2.65])
    # Построение графика
    plt.plot(x, y, 'r-')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.title('Прямоугольник')
    plt.xlim(-1, base + 1)  # Установка границ по оси X
    plt.ylim(-1, height + 1)  # Установка границ по оси Y
    plt.grid(True)
    plt.show()
    
    #rectangle(2,4)
# Трапеция
def Trapezoid(base,height):
    x = np.array([0, 0, 0.5, 1.5, 2, 2 , 0]) 
    y = np.array([0, 2.5 , 3, 3, 2.5, 0 ,0])
    # Построение графика
    plt.plot(x, y, 'b--')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.title('Трапеция')
    plt.xlim(-1, base + 1)  # Установка границ по оси X
    plt.ylim(-1, height + 1)  # Установка границ по оси Y
    plt.grid(True)
    plt.show()
    #Trapezoid(2,4)
# Круг
def circle():
    # Радиус круга
    radius = 2
    # Создание массива углов от 0 до 2π с шагом 0.01
    theta = np.linspace(0, 2*np.pi, 100)
    # Вычисление координат точек круга
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    # Построение круга
    plt.plot(x, y, 'r--')  # 'r-' - красный цвет, сплошная линия
    # Настройка графика
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.title('Круг')
    plt.grid(True)
    plt.axis('equal')  # Сохранение пропорций осей
    # Отображение графика
    plt.show()
# Овал
def Oval():
    # Параметры овала
    a = 3  # Большая полуось
    b = 2  # Малая полуось

    # Создание массива углов от 0 до 2π с шагом 0.01
    theta = np.linspace(0, 2*np.pi, 100)

    # Вычисление координат точек овала
    x = a * np.cos(theta)
    y = b * np.sin(theta)

    # Построение овала
    plt.plot(x, y, 'r-')  # 'r-' - красный цвет, сплошная линия

    # Настройка графика
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.title('Овал')
    plt.axis('equal')  # Сохранение пропорций осей

    # Отображение графика
    plt.show()


