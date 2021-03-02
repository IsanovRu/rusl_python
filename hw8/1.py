# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
# виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Data:
    def __init__(self, day, mother, year):
        self.day = day
        self.mother = mother
        self.year = year
    @classmethod
    def date_real(cls, day, mother, year):
        cls.day = int(day)
        cls.mother = int(mother)
        cls.year = int(year)
    @staticmethod
    def date_valeo():
       str(input('введите число от 1 до 30 - '))
       str(input('введите месяц от 1 до 12 - '))
       str(input('введите год от 1900 до 2050 - '))
data =Data(10,10,10)

data.day
Data.date_valeo()
print(Data.date_real)
