# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный
# метод.
import time
class TrafficLight():
    print('пример светофора red 7сек, yellow 2сек, green 10сек.')
    def __init__(self, colors_times=None):
        if colors_times:
            self.__colors_times = colors_times
        else:
            self.__colors_times = (('red', 7), ('yellow', 2), ('green', 10))
        self.__color = None
    def running(self):
        for ct in self.__colors_times:
            self.__color = ct[0]
            print(self.__color)
            time.sleep(ct[1])
TL = TrafficLight()
TL.running()
print('светофор закончил работать')
