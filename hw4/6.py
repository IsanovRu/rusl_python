# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
#  Например, в первом задании выводим целые числа, начиная с 3, а при
# достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть
# условие, при котором повторение элементов списка будет прекращено.
from itertools import cycle, count

for el in count(3):  # итератор генерирующий
    if el > 10:
        break
    else:
        print(el)
for el in count(2, 3):  # начать с 2 c шагом 3
    if el > 100:  # остановка цикла иначе бесконечность
        break
    else:
        print(el)
C = 0
for el in cycle("ABCDE"):  # итератор повторения
    if C > 5:  # остановка цикла перебор букв 5 раз
        break
    else:
        print(el)
        C += 1
