import random

N = int(input("Enter length: "))

list1 = [random.randint(0, 11) for i in range(N)]
list2 = [random.randint(0, 11) for i in range(N)]

print(list1)
print(list2)
print(*[i for i in list1 if i not in set(list2)])