# Урок 9

# Задача 1 

print('Требуется выяснить сколько чисел различных')
n = int(input('Введите количество чисел (1 ≤ N ≤ 100000): '))

numberList = list(map(int, input('Введите числа через пробел, каждое не превышает 2*10e9 по модулю ').split()))[:n]

numberSet = set(numberList)

print('Ответ ', len(numberSet))


# Задача 2 

print('Вводятся два списка чисел')
aList = list(map(int, input('Введите числа через пробел, до 100000: ').split()))
bList = list(map(int, input('Введите числа через пробел, до 100000: ').split()))
sumList = aList + bList
print(sumList)
cSet = set(sumList)
print(cSet)
print(len(cSet))


# Задача 3

print('Числа встречающиеся последовательности')
nSet = set()

nList = list(map(int, input('Введите числа через пробел ').split()))

for num in nList:
    if num not in nSet:
        nSet.add(num)
        print('No')
    else:
        print('Yes')

