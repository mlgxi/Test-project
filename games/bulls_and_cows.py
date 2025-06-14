from misc.utils import clear, input_number


class BullGame:
    def __init__(self, numbers_count):
        self.game = True
        self.numbers_count = int(numbers_count)
        self.number_sequence = []
        self.user_sequence = []
        self.tries_results = ["\nВаши попытки:"]
        self.tries_count = 0
        self.rules = 'В игре "Быки и коровы" ваша задача разгадать последовательность из нескольких цифр.\nЗа каждую угаданную цифру, стоящую на своём месте, вы получите быка.\nЗа каждую угаданную цифру, стоящую на другом месте, вы получите корову.\nВ последовательности нет двух одинаковых цифр.\nПопробуйте разгадать всю последовательность за минимальное число попыток.'

    def _create_number_sequence(self):
        """Загадывает случайную последовательность цифр для игры"""
        from random import sample
        self.number_sequence = sample("0123456789", self.numbers_count)

    def _input_user_sequence(self):
        """Обрабатывает ввод пользовательской последовательности"""
        # print(self.number_sequence) # Для программиста-тугодума, который не может пройти собственную игру
        print(f"Введите {self.numbers_count} разных цифр: ", end="")
        while True:
            user_input = input()
            if user_input.isdigit():
                if len(user_input) == self.numbers_count:
                    if len(set(user_input)) == len(user_input):
                        return list(user_input)
                    else:
                        print("Все цифры должны быть разные: ", end="")
                else:
                    print(f"Ровно {self.numbers_count} цифр: ", end="")
            else:
                print("Только цифры: ", end="")

    def _compare_sequences(self, user_sequence, number_sequence):
        """Сравнивает пользовательскую последовательность с угаданной"""
        self.tries_count += 1
        bulls = cows = 0
        ends = {
            "bulls": ["ов", ""] + ["а"] * 3 + ["ов"] * 5,
            "cows": ["ов", "ова"] + ["овы"] * 3 + ["ов"] * 5
        }
        for i in range(self.numbers_count):
            if user_sequence[i] == number_sequence[i]:
                bulls += 1
            elif user_sequence[i] in number_sequence:
                cows += 1
        round_result = f"{self.tries_count}) {" ".join(user_sequence)} - {bulls} бык{ends['bulls'][bulls]} и {cows} кор{ends['cows'][cows]}"
        self.tries_results.append(round_result)
        if bulls == self.numbers_count:
            self.game = False

    def _congratulation(self):
        def ends(n):
            if 11 <= n%100 <= 14:
                return "ок"
            elif 1<= n%10 <= 4:
                return (["","ку"]+["ки"]*3)[n%10]
            else:
                return "ок"

        print(r"""
    \|/          (__)    
         `\------(oo)
           ||    (__) Поздравляю! Му-у!
           ||w--||     \|/
       \|/        """)
        print(f"Вы разгадали все цифры за {self.tries_count} попыт{ends(self.tries_count)}")

    def run(self):
        self._create_number_sequence()
        clear()
        print(self.rules)
        while self.game:
            print(*(result for result in self.tries_results if len(self.tries_results) > 1), sep="\n")
            print()
            self.user_sequence = self._input_user_sequence()
            self._compare_sequences(self.user_sequence, self.number_sequence)
            clear()
        self._congratulation()


def start():
    """Начинает игру "Быки и коровы", позволяя выбрать длину цифровой последовательности для угадывания"""
    clear()
    print(r"""
    \|/          (__)    
         `\------(oo)
           ||    (__)
           ||w--||     \|/
       \|/        """)
    print('"Быки и коровы"')
    print(
        'В этой игре вам надо разгадать числовую последовательность за минимальное количество попыток. Чем длиннее последовательность, тем сложнее её восстановить.')
    while True:
        numbers_count = input_number(5, 10, 'Сколько цифр вы хотите отгадать? (5-10): ')
        bg = BullGame(numbers_count)
        bg.run()
        while True:
            next_game = input("Ещё партию? (y/n): ").lower()
            if next_game == "y":
                break
            elif next_game == "n":
                print("Спасибо за игру!")
                exit(0)
