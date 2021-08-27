# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random
N = 10
a = []
for i in range(N):
    a.append(int(random.random() * 200 - 50))
    print("%4d" % a[i], end='')
print()

imin=a.index(min(a))
imax=a.index(max(a))
if imin>imax:
    imax, imin = imin, imax
sum = 0
print("min",min(a))
print("max",max(a))
print("сумма м/у мин макс ")
for i in range(imin+1, imax):
    print(a[i], end=', ')
    sum += a[i]
print()
print('Ответ', sum)
