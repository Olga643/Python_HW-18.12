#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


my_list = []

for i in range(10):
    amount = random.randint(0, 2)
    my_list.append(round(random.uniform(0, 10), amount))

print(my_list)

cut_list = []
x = 0
for i in range(10):
    x = my_list[i] - int(my_list[i])
    x = round((x), 3)
    cut_list.append(x)

print(cut_list)

max = cut_list[0]
min = 1
difference = 0
for i in range(10):
    if cut_list[i] > max:
        max = cut_list[i]
    elif (cut_list[i] != 0) and (cut_list[i] < min):
           min = cut_list[i]

print(f'Максимальная дробная часть: {max}')
print(f'Минимальная  дробная часть: {min}')
print(f'Разность: {max - min}')