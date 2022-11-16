import random

listA = []
n = int(input('Введите количество множеств'))
for i in range(n):
    set1 = set(map(int, input("Введите числа:").split()))
    listA.append(set1)
print(listA)
for j in listA[1:]:
    print(j)
    for i in j:
        if i % 3 == 0 and i not in listA[0]:
            print(i)











#for element in mySet:
   # if element % 3 == 0:
        #newSet.add(element)
#print("Исходное множество:")
#print(mySet)
#print("Новое множество:")
#print(newSet)