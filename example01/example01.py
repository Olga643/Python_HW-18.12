# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


my_list = []

for i in range(5):
    my_list.append(int(random.uniform(0, 10)))
print(my_list)
sum = 0
for i in range (len(my_list)):
    if i % 2 !=0:
        sum = sum + my_list[i]
print(sum)