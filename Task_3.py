# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

from Funct import input_pos_num

num_n = input_pos_num("Введите N: ")

dict_of_num = {}

for i in range(1,num_n+1):
    dict_of_num[i] = (1+1/i)**i
print(dict_of_num)

res = 0

for i in dict_of_num:
    res += float(dict_of_num[i])
print(f"Сумма чисел последовательности = {res:.2f}")