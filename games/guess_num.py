#пользователь угадывает загаданное программой число в выбранном им диапазоне
import random

def numbers():
    num1  = int(input('come up with the beginning of the range: '))
    num2 = int(input('come up with the end of the range: '))
    random_num = random.randint(num1,num2)
    print('great! I imagined a number, try to guess it!')

#в разработке
