# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name.strip()
        if len(str(self.name)) <= 1:
            raise ValueError('Имя не менее 1 символов')
        self.surname = surname
        if len(str(self.name)) <= 1:
            raise ValueError('Имя не менее 1 символов')
        self.position = str(position)
        self._income = {'profit': wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"ФИО сотрудника: {self.name} {self.surname}"

    def get_full_profit(self):
        return f"Доход с пермии: {sum(self._income.values())} руб."


manager = Position(input('Введите имя - '), input('Введите фамилию - '), "CEO", 50000, 125000)
print(manager.get_full_name())
print("Должность: ", manager.position)
print(manager.get_full_profit())