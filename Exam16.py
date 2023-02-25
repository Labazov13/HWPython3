from random import randint
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

countNumbers=int(input("Введите количество чисел: "))

list_1=[randint(0,11) for i in range(countNumbers)]
print(list_1)
searchNumber=int(input("Введите искомое число: "))
count=0
for i in range(len(list_1)):
    if list_1[i]==searchNumber:
        count+=1
print(count)