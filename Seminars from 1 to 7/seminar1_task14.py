# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k ), не превосходящие числа N.
# 10 -> 1 2 4 8

N = int(input("Введите число N: "))
p = 1
print(N, "-> ", end=' ')
while p <= N:
    print(p, end=' ')
    p = p * 2