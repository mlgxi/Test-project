from games import guess_num
from games import bulls_and_cows
from games import wordle

def game():
    print('1. Guess a number',
          '2. Bulls and cows',
          '3. Wordle',
          '...',sep='\n')
    num = int(input('Choose a num for game: '))
    if num == 1:
        guess_num.numbers()
    elif num == 2:
        bulls_and_cows.start()
    elif num == 3:
        wordle.start()

if __name__ == '__main__':
    game()