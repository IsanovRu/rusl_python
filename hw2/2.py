# 2.	Для списка реализовать обмен значений соседних элементов.\
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. \
# При нечётном количестве элементов последний сохранить на своём месте. \
# Для заполнения списка элементов нужно использовать функцию input().
l = list(input('введите любое слово будет реверс - '))
for a in range(0, len(l), 2):
    l[a:a + 2] = l[a - len(l) + 1:a - 1 - len(l):-1]
print(l)