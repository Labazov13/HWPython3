import random
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

countNumbers=int(input("Введите количество чисел: "))
list_1=[random.randint(0,13) for i in range(countNumbers)]
#list_1=[i for i in range(countNumbers)]
print(list_1)
max=list_1[0]

searchNumber=int(input("Введите искомое число: "))

for i in range(len(list_1)):
    if list_1[i]>max:
        max=list_1[i]
    if list_1[i]==searchNumber:
        print(list_1[i])
        break

if searchNumber not in list_1:
    if searchNumber>max:
        print(max)
    else:
        lesserNumber=searchNumber-1
        moreNumber=searchNumber+1
        for i in range(len(list_1)):
            if list_1[i]==lesserNumber or list_1[i]==moreNumber:
                print (list_1[i])
                break



                
    
                
