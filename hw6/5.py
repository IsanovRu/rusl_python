# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и
# проверить, что выведет описанный метод для каждого экземпляра.
class Stationary:

    def __init__(self, title="Что умеешь рисовать"):
        self.title = title
        while self == str(self):
            if self == Pen:
                Pen.draw()
            elif self == Pencil:
                Pencil.draw()
            elif self == Marker:
                Marker.draw()
        # else:
        #     e


    def draw(self):
        print(f'Просто начни рисовать! {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Просто начни рисовать ручкой(pen)! {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Просто начни рисовать карандашом(Pencil)! {self.title}')


class Marker(Stationary):
    def draw(self):
        print(f'Просто начни рисовать маркером(Marker)! {self.title}')

stat = Stationary(str.capitalize(input('чем хочите рисовать:выбирете Pen, Pencil, Marker - ')))
stat.draw
# mark = Marker()
# pen = Pencil()
#
# mark.draw()
# pen.draw()