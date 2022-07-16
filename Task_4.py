# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

import time

str_time = str(time.time_ns())

list_of_num = [1,2,3,4,5,6,7,8,9,10]
print(list_of_num)

for i in range(0,len(list_of_num)):
    for j in str_time:
        if int(j) < len(list_of_num):
            list_of_num[i],list_of_num[int(j)] = list_of_num[int(j)],list_of_num[i]

print(list_of_num)