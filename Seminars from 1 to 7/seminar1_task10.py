# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0 2
# *Какое минимальное количество раз нужно перевернуть монеты, что бы они были все одной стороной.
N = int(input("Введите кол-во монет: "))
from random import randint
random_list=[]
for i in range(N):
    random_list.append(randint(0,1))
print(random_list)
eagle = 0
tails = 0
for random_list in random_list:
    if random_list == 1: eagle = eagle + 1
    if random_list == 0: tails = tails + 1
if eagle > tails: print(tails)
else: print(eagle)