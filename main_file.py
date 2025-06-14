from games import guess_num
from games import bulls_and_cows

def game():
    print('1. Guess a number',
          '2. Bulls and cows',
          '...',sep='\n')
    num = int(input('Choose a num for game: '))
    if num == 1:
        guess_num.numbers()
    elif num == 2:
        bulls_and_cows.start()

if __name__ == '__main__':
    game()