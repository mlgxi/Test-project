class BullGame:
    def __init__(self, numbers_count):
        self.numbers_count = numbers_count
        pass
    def run(self):
        pass

def start():
    """Начинает игру "Быки и коровы", позволяя выбрать длину цифровой последовательности для угадывания"""
    print('Начинаем игру "Быки и коровы"')
    print('Начинаем игру "Быки и коровы"')
    numbers_count = input('Сколько цифр вы хотите отгадать? (5-10): ')
    bg = BullGame(numbers_count)
    bg.run()