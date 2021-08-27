# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться
import random
N = 10
a = []
for i in range(N):
    a.append(int(random.random() * 100))
    print("%3d" % a[i], end='')
print()
a.sort()
print(a[0])
print(a[1])
