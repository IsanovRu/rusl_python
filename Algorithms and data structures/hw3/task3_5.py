# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
N = 10
a = []
for i in range(N):
    a.append(int(random.random() * 200 - 50))
    print("%4d" % a[i], end='')
print()
b = a.copy()
a.sort()
for i in range(N):
    if a[i]>=0:
        ii = b.index(a[i-1])
        print(f'позиция в массиве :{ii+1}\nмах отрицательный элемент :{a[i-1]}')
        break