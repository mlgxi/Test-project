#пользователь угадывает загаданное программой число в выбранном им диапазоне
import random

def numbers():
    num1  = int(input('come up with the beginning of the range: '))
    num2 = int(input('come up with the end of the range: '))
    random_num = random.randint(num1,num2)
    attempt = 0
    points = 0
    try_guess = int(input('great! I imagined a number, try to guess it!'))
    if try_guess == random_num:
        print(f'Ur guess, {try_guess} is correct! Attempts: {attempt}')
    else:
        middle = num2 // 2
        while not try_guess == random_num:
            print('sm')

#в разработке
