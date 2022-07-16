# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*
# 6782 -> 23
# 0,56 -> 11

from Funct import input_number_test_float

number = str(input_number_test_float("Введите число: "))

res = 0

for i in number:
    if i.isdigit():
        res = res + int(i)

print(f"Сумма цифр в числе {number} равна {res}")