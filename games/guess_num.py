import random

def numbers():
    '''пользователь угадывает загаданное программой число в выбранном им диапазоне'''
    print('\n\t Welcome to the game! Ur should guess a number what I\'ll imagine! \n')
    points = 0
    def inner():
        while True:
            minn = int(input('come up with the beginning of the range: '))
            maxx = int(input('come up with the end of the range: '))
            random_num = random.randint(minn, maxx)
            nonlocal points
            attempt = 0
            try_guess = int(input('\n great! I imagined a number, try to guess it! \n\t'))

            while True:
                if try_guess > random_num:
                    try_guess = int(input('your number is too big, try guess again: \n\t'))
                    attempt += 1
                elif try_guess < random_num:
                    try_guess = int(input('your number is too small, try guess again: \n\t'))
                    attempt += 1
                else:
                    print(f'Ur guess, {try_guess} is correct!\n')
                    attempt += 1
                    break
            if attempt < 4: points += 3
            elif 4 <= attempt < 7: points += 2
            else: points += 1
            finish = input(f'The game has finished! Attempts: {attempt}, points: {points} \n'
                           f'Do you want play again? \n\t')
            if finish == 'Yes' or finish == 'yes':
                numbers()
            elif finish == 'No' or finish == 'no':
                print('Goodbye!')
                return points
    inner()