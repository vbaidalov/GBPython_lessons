# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких
# собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

# N = int(input("Введите количество кустов: "))
#
# from random import randint
#
# harvest = []
# for i in range(N):
#        harvest.append(randint(0, 20))
# print("Количество ягод на кустах: ", harvest)
#
# max_harvest = 0
# temp = 0
# for harvest[1] in range(len(harvest)):
#        if (harvest[i] > harvest[0] and harvest[i] < harvest[len - 1]):
#               temp = (harvest[i - 1]) + harvest[i] + (harvest[i + 1])
#               if (max_harvest < temp):
#                      max_harvest = temp
# print(max_harvest)


N = int(input("Введите количество кустов: "))
from random import randint
harvest = list()
for i in range(N):
        harvest.append(randint(0, 20))
print("Количество ягод на кустах: ", harvest)

# n = int(input())
# arr = list()
# for i in range(n):
#        x = int(input())
#        arr.append(x)

arr_count = list()
for i in range(len(harvest) - 1):
       arr_count.append(harvest[i - 1] + harvest[i] + harvest[i +1])
arr_count.append(harvest[-2] + harvest[-1] + harvest[0])
print(max(arr_count))

