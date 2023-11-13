import random

def play_game():
    word_list = ['apple', 'ball', 'cat', 'dog', 'elephant', 'giraffe', 'house', 'tree', 'water', 'mountain', 'river', 'lake', 'cloud', 'sky', 'sun']
    word = random.choice(word_list)
    print('The word has ' + str(len(word)) + ' letters. Enter your guesses.')

    guesses = ''
    attempt = 1
    while attempt <= 5:
        print('Enter a letter:')
        guesses += input()
        count = 0
        for letter in word:
            if letter in guesses:
                count += 1
                print(f'Guessed {count} letters')
        
        if count == len(word):
            print('You guessed the word!')
            break

        if attempt == 3:
            print('Hint: The word starts with ' + word[0])
        
        attempt += 1
    
    print('Do you want to play again? Enter y or n')
    if input() == 'y':
        play_game()
    else:
        print('Goodbye!')

play_game() 

