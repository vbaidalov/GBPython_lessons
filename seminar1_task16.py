# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3 -> 1


N = int(input("Введите размер списка: "))

from random import randint

list = []
for i in range(N):
    list.append(randint(-9, 9))
print(list)

X = int(input("Число поиска Х: "))

count = 0
for i in range(len(list)-1):
    if list[i] == X:
        count = count + 1
print(count)