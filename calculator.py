# Калькулятор
import math

def calculator():
    '''
    Основная функция в которой будут вызываться функции
    '''
    print('какой калькулятор запустить?')
    z = 0
    z += int(input('1 -- обычный /2 -- инжинерный '))
    if z == 1: 
        simple_calculator()
    if z == 2:    
        engineering_calculator()
         
def simple_calculator():
   
    '''
    Обычный калькулятор
    '''

    what_to_do_c = ''
    what_to_do = 0 # в этой переменной хранится ввод (для обычного калькулятора).
    what_to_do += float(input('\n Введите число '))
    what_to_do_c += input('\n C, +, -, *, /, //, %, sqrt,** ')

    if what_to_do_c == 'c' or 'C': # чистит res
        res = 0
        # print('Ваше итоговое выражение имеет вид = ', res)

    if what_to_do_c == '+': # plus
            plus = float(input('Введите число '))
            z = []
            z.append(what_to_do)
            res = float(''.join(map(str, z))) #  перводим список в число через преобразование строк.
            z = res
            q = 0
            q += int(input('Прибавить к существующему результату? 1 -- да /2 -- нет '))
            if q == 1:
                final_expression_plus = res + plus
                print('Ваше итоговое выражение имеет вид = ', final_expression_plus)
                return simple_calculator()
            if q == 2:
                print('Программа остановлена.')
                 
    if what_to_do_c == '-': # minus
            minus = float(input('Введите число '))
            z_1 = []
            z_1.append(what_to_do)
            res = float(''.join(map(str, z_1))) #  перводим список в число через преобразование строк.
            z_1 = res
            q = 0
            q += int(input('Вычесть из существующего результата? 1 -- да /2 -- нет '))
            if q == 1:
                final_expression_minus = res - minus
                print('Ваше итоговое выражение имеет вид = ', final_expression_minus)
                return simple_calculator()
            if q == 2:
                print('Программа остановлена.')
            
    if what_to_do_c == '*': # умножение
            multiply = float(input('Введите число '))
            z_2 = []
            z_2.append(what_to_do)
            res = float(''.join(map(str, z_2))) #  перводим список в число через преобразование строк.
            z_2 = res
            q = 0
            q += int(input('Умножить на данное число? 1 -- да /2 -- нет '))
            if q == 1:
                final_expression_multiply = res * multiply
                print('Ваше итоговое выражение имеет вид = ', final_expression_multiply)
                return simple_calculator()
            if q == 2:
                print('Программа остановлена.')

    if what_to_do_c == '**': # возведение в степень.
            p_w = int(input("В какую степень хотите возвезти? ")) # хранится степень числа.
            z_3 = []
            z_3.append(what_to_do)
            res = int(''.join(map(str, z_3))) #  перводим список в число через преобразование строк.
            z_3 = res
            q = 0
            q += int(input('Возвезти на текущую степень? 1 -- да /2 -- нет '))
            if q == 1:
                final_expression_pow = (pow(res,p_w))
                print('Ваше итоговое выражение имеет вид = ', final_expression_pow)
                return simple_calculator()
            if q == 2:
                print('Программа остановлена.')

    if what_to_do_c == '/': # деление с плавоющей точкой.
            z_4 = []
            z_4.append(what_to_do)
            res = float(''.join(map(str, z_4))) #  перводим список в число через преобразование строк.
            z_4 = res
            q = 0
            question = float(input('Введите на сколько поделить '))
            q += int(input('Разделить текущие число? 1 -- да /2 -- нет '))
            if q == 1:
                final_expression_dot_division = (res / question)
                print('Ваше итоговое выражение имеет вид = ', final_expression_dot_division)
                return simple_calculator()
            if q == 2:
                print('Программа остановлена.')

    if what_to_do_c == '//': # истинное деленение.
            z_5 = []
            z_5.append(what_to_do)
            res = float(''.join(map(str, z_5))) #  перводим список в число через преобразование строк.
            z_5 = res
            q = 0
            question = float(input('Введите на сколько поделить '))
            q += int(input('Разделить текущие число (истинное деление)? 1 -- да /2 -- нет '))
            if q == 1:
                final_expression_true_division = (res // question)
                print('Ваше итоговое выражение имеет вид = ', final_expression_true_division)
                return simple_calculator()
            if q == 2:
                print('Программа остановлена.')

    if what_to_do_c == '%': # процент от числа .
            # nums = int(input('Введите число '))
            z_6 = []
            z_6.append(what_to_do)
            res = float(''.join(map(str, z_6))) #  перводим список в число через преобразование строк.
            z_6 = res
            q = 0
            q += int(input('Посчитать проценты? 1 -- Число в процентах /2 -- Процент от числа 3 -- стоп '))
            if q == 1:            
                res_proc = what_to_do / 100
                print('Число в процентах = ',res_proc)
                return simple_calculator()
            if q == 2:
                procent = float(input('Введите процент '))
                res_proc =  (what_to_do * (procent / 100))
                print('Процент от числа = ', res_proc)
                return simple_calculator()
            if q == 3:
                print('Программа остановлена')

    if what_to_do_c == 'sqrt': # вычисляем корень
        res = math.sqrt(what_to_do) # Извлекает квадратный корень, сохраняем значение в новой переменной. 
        print('Ваше итоговое выражение имеет вид = ', res )

def engineering_calculator():
    
    '''
    Представляет из себя инженерный калькулятор
    '''
    num = float(input('Введите начальное число '))
    what_to_do_math = 0
    what_to_do_math += int(input('\n 1 -- Округлить вниз \n 2 -- Округлить вверх \n 3 -- Взять модуль числа\
    \n 4 -- Извлечь квадратный корень \n 5 -- Возвезти экспоненту в степень равную числу\
    \n 6 -- Посчитать натуральный логарифм числа \n 7 -- Посчитать логарифм числа по основанию 2\
    \n 8 -- Посчитать логарифм числа по основанию 10  \n 9 -- Посчитать синус числа\
    \n 10 -- Посчитать косинус числа \n'))
    
    if what_to_do_math == 1: # Округляет вниз
        round_up = math.floor(num) 
        print('%.6f' % round_up)
        what_to_do_math = 0
        engineering_calculator()

    if what_to_do_math == 2: # Округляет вверх
        roll_down = math.ceil(num)  
        print('%.6f' % roll_down)
        what_to_do_math = 0
        engineering_calculator()

    if what_to_do_math == 3: # Берет модуль числа
        num = math.fabs(num)  
        print('%.6f' % num)
        what_to_do_math = 0
        engineering_calculator()

    if what_to_do_math == 4: # Извлекает квадратный корень
        num = math.sqrt(num)  
        print('%.6f' % num)
        what_to_do_math = 0
        engineering_calculator()

    if what_to_do_math == 5: # Возводит экспоненту в степень, равную числу
        num = math.exp(num) 
        print('%.6f' % num)
        what_to_do_math = 0
        engineering_calculator()

    if what_to_do_math == 6: # Считает натуральный логарифм числа
        num = math.log1p(num) 
        print('%.6f' % num)
        what_to_do_math = 0
        engineering_calculator()

    if what_to_do_math == 7: # Считает логарифм числа по основанию 2
        num = math.log2(num) 
        print('%.6f' % num)
        what_to_do_math = 0
        engineering_calculator()

    if what_to_do_math == 8: # Считает логарифм числа по основанию 10
        num = math.log10(num) 
        print('%.6f' % num)
        what_to_do_math = 0
        engineering_calculator()

    if what_to_do_math == 9: # Считает синус
        sin = math.sin(num) 
        print('%.6f' % sin)
        print(math.degrees('%.6f' % sin))
        what_to_do_math = 0
        engineering_calculator()

    if what_to_do_math == 10: # Считает косинус
        cos = math.cos(num) 
        print('%.6f' % cos) # выводит значение в радианах 
        print(math.degrees('%.6f' % cos)) # переводим в градусы
        what_to_do_math = 0
        engineering_calculator()

    
calculator()
