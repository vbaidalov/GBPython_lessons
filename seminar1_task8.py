# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

N = int(input("Введите кол-во арбузов: "))

import random
watermelon = random.sample(range(1, 20), N)
print(watermelon)
watermelonMAX = watermelon[0]
watermelonMIN = watermelon[0]

for i in range(len(watermelon)):
    if watermelon[i] > watermelonMAX: watermelonMAX = watermelon[i]
for i in range(len(watermelon)):
    if watermelon[i] < watermelonMIN: watermelonMIN = watermelon[i]

print(watermelonMAX)
print(watermelonMIN)

# a=[1,3,6,8,3,23,6,8,5,3,45,6,8,5,3]
# max = a[0]
# pos = 0
# for i in range(len(a)):
#     if a[i]>max: max=a[i];pos=i
# print ("max=",max,", pos=",pos)
