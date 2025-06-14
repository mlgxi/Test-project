from misc.utils import clear, input_number


class BullGame:
    def __init__(self, numbers_count):
        self.numbers_count = int(numbers_count)
        self.number_sequence = []
    def _create_number_sequence(self):
        from random import randint
        self.number_sequence = [randint(0, 9) for _ in range(self.numbers_count)]

    def run(self):
        clear()
        self._create_number_sequence()
        while True:
            print(self.number_sequence)
            input()

def start():
    """Начинает игру "Быки и коровы", позволяя выбрать длину цифровой последовательности для угадывания"""
    clear()
    print('Начинаем игру "Быки и коровы"')
    print('В этой игре вам надо разгадать числовую последовательность за минимальное количество попыток. Чем длиннее последовательность, тем сложнее её восстановить.')
    numbers_count = input_number(5,10,'Сколько цифр вы хотите отгадать? (5-10): ')
    bg = BullGame(numbers_count)
    bg.run()