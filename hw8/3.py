# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и
# заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
class MyBadError(Exception):
    def __init__(self, txt):
        self.txt = int(txt)
        try:

        except Exception as e:
            print('разрешено вводить только числа')

    def bad_func(self):
        b = args
        try:
          while i == args:
               args.append(int(input('введите данные')))
    # a = input()
          if b == 'n':
            print('end')
        except Exception as e:
            print('все накрылось')
my = MyBadError()
# print(my.bad_func(input('ведите числа - ')))
my.bad_func(000)
