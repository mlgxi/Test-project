class BullGame:
    def __init__(self, numbers_count):
        self.numbers_count = numbers_count
        pass
    def run(self):
        while True:
            pass


def start():
    """Начинает игру "Быки и коровы", позволяя выбрать длину цифровой последовательности для угадывания"""
    print('Начинаем игру "Быки и коровы"')
    print('В этой игре вам надо разгадать числовую последовательность за минимальное количество попыток. Чем длиннее последовательность, тем сложнее её восстановить.')
    numbers_count = input('Сколько цифр вы хотите отгадать? (5-10): ')
    bg = BullGame(numbers_count)
    bg.run()