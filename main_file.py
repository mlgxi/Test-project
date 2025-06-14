from games import guess_num

def game():
    print('1. Guess a number',
          '2.',
          '...',sep='\n')
    num = int(input('Choose a num for game: '))
    if num == 1:
        guess_num.numbers()

if __name__ == '__main__':
    game()