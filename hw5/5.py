# Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import os
# f_o = open("hw5.txt", "r")
s=open("hw5.txt", "r")


def sum(x=0):
    s=s.read()
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


#""" s = str(input("Введите числа через пробел (закончить 'Q') -"))""""
f_o.close()
# f=open("data.txt","w")
# s=(f.read())
# a=s.split(',')#вместо запятой может бить точка, любой символ
# print(a)   #(если у вас в файле дание через пробел топишем  пробел, через точку-точку)
# f.close(
# s = (f_obj.wre())
#     while f_obj:
#         a = (input('введи данные(чтобы завершить введите пробел) - '))
#         print(a, file=f_obj)
#         if a == ' ':
#             break
