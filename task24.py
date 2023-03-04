# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой
# грядке, причем кусты высажены только по окружности. Таким образом, у каждого
# куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты
# обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском
# хозяйстве внедрена система автоматического сбора черники. Эта система
# состоит из управляющего модуля и нескольких собирающих модулей. Собирающий
# модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом.
# Пользователь вводит список содержащий количество ягод на кустах.
# Input: 2 2 1 3 2
# Output: 7
from addInterface import creat_int_list

list_ber = creat_int_list(50, 1, 5)
print(*list_ber)
num_bush = len(list_ber)
max_ber = list_ber[num_bush - 2] + list_ber[num_bush - 1] + list_ber[0]
bushes = f"{num_bush - 1}, {num_bush}, {0}"
cur_ber = 0
for i in range(num_bush - 2):
    cur_ber = list_ber[i - 1] + list_ber[i] + list_ber[i + 1]
    if cur_ber > max_ber:
        max_ber = cur_ber
        bushes = f"{i}, {i + 1}, {i + 2}"
print(f"Максимум ягод - {max_ber}(кусты - {bushes})")
