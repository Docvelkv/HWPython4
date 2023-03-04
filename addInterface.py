from random import randint as irand, random as frand


def correct_int() -> int:
    """
    Ввод целого числа с обработкой некорректного введения.\n
    Возвращает целое число или предлагает ввести снова.
    """
    is_correct = True
    while is_correct:
        num_int = input()
        try:
            num_int = int(num_int)
            is_correct = False
            return num_int
        except ValueError:
            print("Это не целое число. Введите снова:")


def creat_int_list(num_elm=10, min_val=0, max_val=10):
    """
    Создание списка из целых чисел.\n
    num_elm - количество элементов списка.\n
    min_val - начало диапазона.\n
    max_val - конец диапазона.\n
    Все аргументы необязательные.
    """
    list_1 = [irand(min_val, max_val) for i in range(num_elm)]
    return list_1


def creat_float_list(num_elm=10, min_val=0, max_val=10, num_dig=1):
    """
    Создание списка из вещественных чисел.\n
    num_elm - количество элементов списка.\n
    min_val - начало диапазона.\n
    max_val - конец диапазона.\n
    num_dig - количество цифр после запятой.\n
    Все аргументы необязательные.
    """
    list_1 = [irand(min_val, max_val) + round(frand(), num_dig)
              for i in range(num_elm)]
    return list_1
