# Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    """Автомобиииль !!!"""

    def __init__(self, name, color, speed, is_police=False):
        self.name = name.strip()
        if len(self.name) < 1:
            raise ValueError('Имя не менее 1 символов')
        self.color = color
        self.speed = abs(float(speed))
        if self.speed > 500:
            raise ValueError('\033[032m Нереальная скорость автомобиля')
        self.is_police = is_police
        print(f"\033[34m Новая машина: \033[0m{self.name} (Цвет {self.color}) \033[31m машина полицейская -"
              f" \033[0m {self.is_police}")

    def go(self):
        print(f"{self.name}: \033[32mМашина поехала")

    def stop(self):
        print(f"{self.name}: \033[31m Машина остановилась")

    def turn(self, direction):
        print(f"{self.name}: Машина повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print(f"{self.name}: Скорость автомобиля - {self.speed}")

class WorkCar(Car):

    def show_speed(self):
        return f"{self.name}: \033[34m Скорость автомобиля - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!!!" \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля - {self.speed}" # super().show_speed()


class SportCar(Car):
    """Спортивный автомобилб"""

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

police_car = PoliceCar('ДПС', 'Белый', 80)
police_car.go()
