# Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...Количество элементов (n)
# вводится с клавиатуры.
n = int(input("Количество элементов: "))
m = 1
while n > 0:
    print(m, end=' ')
    m = m / -2
    n -= 1
print()