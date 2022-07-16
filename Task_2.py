# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from Funct import input_pos_num

number_n = input_pos_num("Введите N : ")
list_of_num = [1]
for i in range(1,number_n):
    list_of_num.append(list_of_num[i-1]*(i+1))
print(list_of_num)