# 1.	Создать список и заполнить его элементами различных типов данных. \
# Реализовать скрипт проверки типа данных каждого элемента. Использовать \
# функцию type() для проверки типа. Элементы списка можно не запрашивать у \
# пользователя, а указать явно, в программе.
a1 = 123
a1_1 = 123.123
a2 = 'Привет мир привет ветер'
a3 = True
a4 = ['hi', 'by', 'see']
a5 = ('123', 'geek')
a6 = complex(1, 2)
print(type(a1), a1)
print(type(a1_1), a1_1)
print(type(a2), a2, '\n', a2[6:10], a2[::2], a2[::-1])  # []срезы  [::2] срез с шагом 2, зеркальный[::-1]
print(type(a3), a3)
print(type(a4), a4)
print(type(a5), a5)
print(type(a6), a6)
