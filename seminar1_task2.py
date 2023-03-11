# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print("Введите трёхзначное число")
n = int(input())
if (n > 99 and n < 999):
    def getSum(n):

        sum = 0
        while (n != 0):
            sum = sum + (n % 10)
            n = n // 10
        return sum


    print(n, '->', getSum(n))
else:
    print("No, you didn't succeed. try again")