# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint
x, y, a, b = [int(input(i))for i in ("размер матицы x = ", "размер матицы y = ", "случ.число от = ", "до = ")]
matrix = [[randint(a, b) for _ in range(y)] for j in range(x)]
print('матрица')
for i in matrix:
    print(*i)
print(' \nминимальны значения строк\n')
for x_ in range(x):
    print(x_+1, 'строка', 'минимальное', min(matrix[x_]))
    print(x_+1, 'строка', 'max', max(matrix[x_]))
print(' \nминимальны значения столбцов\n')
for x_ in range(y):
    matrix_ = [matrix[i][x_] for i in range(x)]
    print(x_+1, 'столбец', 'минимальное', min(matrix_))
