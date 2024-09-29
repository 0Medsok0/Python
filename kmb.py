import random

def rock_paper_scissors():
    count = 0 # очки пользователя
    count_pc = 0 # очки компьютера

    while count < 3: # до 3 побед 
        x = random.randint(1, 3) 
        question = input('Камень, Ножницы, Бумага: ').lower()
        if x == 1 and question == 'камень': # вариант ничьи записывается в count_pc
            print('Вы проиграли!')
            count_pc += 1
        elif x == 2 and question == 'ножницы':
            print('Вы проиграли!')
            count_pc += 1
        elif x == 3 and question == 'бумага':
            print('Вы проиграли!')
            count_pc += 1
        else:
            print('Вы выиграли!')
            count += 1

    print('Счет','вы:',count,'компьютер:',count_pc)

def guess_the_number():
    q = random.randrange(1,10)
    guess = int(input("Введите любое число: ")) 
    while q!= guess: 
        if guess < q:
            print("Слишком низко")
            guess = int(input("Введите число еще раз: ")) 
        elif guess > q:
            print("Слишком высоко!")
            guess = int(input("Введите число еще раз: "))
        else:
            break
    print("Вы угадали!")

def mainMenu():
    print('Во что хотите сыграть? ')
    question = input('Камень ножницы бумага / Угадай число ? ')
    if question == 'Камень ножницы бумага':
        rock_paper_scissors()
    if question == 'Угадай число':
        guess_the_number()

mainMenu()
