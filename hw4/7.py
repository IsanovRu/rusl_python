# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
#     Функция отвечает за получение факториала числа, а в цикле необходимо выводить
#     только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
#     апример, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
# def sum_num():
#     s=0
#     while True:
#         in_List = input('введите число или Q для выхода - ').split()
#         for num in in_List:
#             if num == 'q':
#                 return s
#             else:
#                 try:
#                     s+=int(num)
#                 except ValueError:
#                     print('Чтобы выйти из программы нажмите q -')
#
#         print(f'сумма чисел = {s}')
# print(sum_num())
# num =0
# try:
#     while num!= 'q':
#         for i in map(int, input('для выхода наберите q Введите число используя пробел - ').split()):
#             num += i
#         print(num)
# except ValueError:
#     print(num)
def my_pow_func(x,y):
    return 1 if y ==0 else my_pow_func(x, y + 1) * 1 / x
print(my_pow_func(2,-3))
