# Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.
n1 = input("Введите целое число: ")
n2 = n1[::-1]
print('"Обратное" ему число:', n2)