"""Подборка функций, которые могут пригодиться в разных местах проекта"""


def clear():
    """
    Очищает консоль.
    Стандартные очистки в консоли PyCharm не работают, потому такой костыль
    """
    print("\n" * 120)


def is_number(s: str) -> bool:
    """Проверяет, является ли строка числом"""
    try:
        float(s)  # Пробуем преобразовать строку в float (это охватит и целые, и вещественные числа)
        return True
    except ValueError:
        return False


def input_number(
        left_limit: int | float = -float('inf'),
        right_limit: int | float = float('inf'),
        welcome: str = "Пожалуйста, введите число: "
) -> int | float:
    """
    Запрашивает у пользолвателя числа до тех пор, пока ввод не удовлетворит условию.

    Args:
        left_limit (int, float): Левая граница числа
        right_limit (int, float): Правая граница числа
        welcome (str): Текст запроса, который показывают пользователю

    Returns:
        int, float: Число, введённое пользователем.
    """
    while True:
        number = input(welcome)
        if is_number(number):
            if "." in number:
                number = float(number)
            else:
                number = int(number)

            if left_limit <= number <= right_limit:
                return number
        print(f'\nВведите число между {left_limit} и {right_limit}')
