from addInterface import creat_int_list

# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах. Пользователь вводит 2 списка:
# 1 строка - первый список через пробел,
# 2 строка - второй список через пробел.

str_1 = " ".join(map(str, creat_int_list(20, 1, 50)))
str_2 = " ".join(map(str, creat_int_list(20, 1, 50)))
print(f"Строки введённые пользователем:\n{str_1}\n{str_2}")
lst_common = f"{str_1} {str_2}".split()
# print("Общий список:", *lst_common)
set_temp = set()
for i in lst_common:
    if i.isnumeric():
        set_temp.add(int(i))
lst_result = [*set_temp]
lst_result.sort()
print("Результат:", *lst_result)
