

items = int(input("Введите размер списка: "))
value = int(input("Введите число для поиска: "))

from random import randint

list = []
for i in range(items ):
    list.append(randint(-9, 9))

def nearest_value(list, value):

    found = list[0]
    for item in list:

        if abs(item - value) < abs(found - value):
            found = item
    return found

print(f'Ближайшее число к {value} в списке {list} является {nearest_value(list, value)}')