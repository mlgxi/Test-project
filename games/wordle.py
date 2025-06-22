from misc.utils import clear, input_number
from games.bulls_and_cows import BullGame


class Wordle(BullGame):
    """
    Основная логика Wordle наследуется от игры "Bulls and Cows" за небольшими исключениями.
    Вместо цифр используются слова.
    """

    def __init__(self, word_length):
        super().__init__(word_length)
        self.rules = 'В игре "Wordle" оно же "Словарные быки и коровы" ваша задача разгадать слово.\nЗа каждую угаданную букву, стоящую на своём месте, вы получите быка.\nЗа каждую угаданную букву, стоящую на другом месте, вы получите корову.\nВ загаданном слове нет двух одинаковых букв.\nПопробуйте разгадать всё слово за минимальное число попыток.'

    def _create_sequence(self):
        """Выбирает случайное слово нужной длины для игры"""
        from random import sample
        self.guessed_sequence = self._get_word_from_db(self.sequence_length)

    def _get_word_from_db(self, word_length, lang='rus'):
        """
        Берёт случайное слово подходящей длины из базы данных.
        Но пока просто из списка слов
        """
        # TODO: Подключить получение слова из базы данных
        from random import choice
        if lang == 'rus':
            from db.russian_words import words
            word = choice(list(words[word_length]))
            return list(word)
        else:
            raise ValueError("No such language! Try lang='rus'.")

    def _find_word_in_db(self, word, lang='rus'):
        """
        Проверяет наличие слова в базе данных.
        Но пока просто в списке слов
        """
        # TODO: Подключить проверку слова в базе данных
        if lang == 'rus':
            from db.russian_words import words
            return word in words[self.sequence_length]
        else:
            raise ValueError("No such language! Try lang='rus'.")

    def _input_user_sequence(self):
        """Обрабатывает ввод пользовательской последовательности"""
        # print(self.guessed_sequence) # Для программиста-тугодума, который не может пройти собственную игру
        print(f"Введите существительное из {self.sequence_length} разных букв: ", end="")
        while True:
            user_input = input().lower()

            if user_input.isalpha():
                if len(user_input) == self.sequence_length:
                    if len(set(user_input)) == len(user_input):
                        if self._find_word_in_db(user_input):
                            return list(user_input)
                        else:
                            print("Не знаю такого слова, попробуйте другое: ", end="")
                    else:
                        print("Все буквы должны быть разные: ", end="")
                else:
                    print(f"Ровно {self.sequence_length} букв: ", end="")
            else:
                print("Слово должно состоять из букв: ", end="")


def start():
    """Начинает игру "Wordle" (Словарные быки и коровы), позволяя выбрать длину слова для угадывания"""
    clear()
    print(r"""
    \|/          (__)    
         `\------(oo)
           ||    (__)
           ||w--||     \|/
       \|/        """)
    print('"Wordle" или же по-русски "Словарные быки и коровы"')
    print(
        'В этой игре вам надо разгадать слово за минимальное число попыток. Чем длиннее слово, тем сложнее его разгадать.')
    while True:
        word_length = input_number(5, 7, 'Какой длины слово хотите отгадать? (5-7): ')
        wg = Wordle(word_length)
        wg.run()
        while True:
            next_game = input("Ещё партию? (y/n): ").lower()
            if next_game in ("y","н","yes","да"):
                break
            elif next_game in ("n","т","no","нет"):
                print("Спасибо за игру!")
                exit(0)
