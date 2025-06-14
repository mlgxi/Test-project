from games import guess_num, bulls_and_cows, naval_battle

def game():
    print('1. Guess a number',
          '2. Bulls and cows',
          '3. naval battle'
          '...',sep='\n')
    num = int(input('Choose a num for game: '))
    if num == 1:
        guess_num.numbers()
    elif num == 2:
        bulls_and_cows.start()
    elif num == 3:
        naval_battle.navalBattle()

if __name__ == '__main__':
    game()