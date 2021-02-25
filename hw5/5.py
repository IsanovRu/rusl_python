# Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import os


s = open("hw5.txt", "w+")


def sum(x=1):
    s = str(input("Введите числа через пробел (закончить 'Q') -"))
    s = s.read()
    arr = s.split(' ')
    for val in arr:
        if val.capitalize() == 'Q':
            print("Cумма = {}".format(x))
            return x
        try:
            x += float(val)
        except Exception as e:
            print ("Ошибка, этот символ - '{}' пропускаем".format(val))
            print("Error! " + str(e))
    print("Cумма = {}".format(x))
    sum(x)
print(sum())
