# Создать программно файл в текстовом формате, записать
# в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
with open("hw1.txt", "a", encoding='utf8') as f_obj:
    while f_obj:
        a = (input('введи данные(чтобы завершить введите пробел) - '))
        print(a, file=f_obj)
        if a == ' ':
            break
with open('1.txt', 'w', encoding='utf8') as f:
    while True:
        line = input('Введите новую строку - ')
        if not line:  # эли пустая строчка нажал enter то закрыть
            break
        f.write(f'{line}\n')  # осуществляем запись
        # print(line, file=f)  # принт f записать в файл
