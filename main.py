# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

Print("Введите трёх значное число")
n = int(input())
if (n > 99 and n < 999):
    print("Ты красавчик")
else:
    print("Ебать ты лох")
