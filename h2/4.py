#Пользователь вводит строку из нескольких слов, разделённых пробелами. \
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.\
# Если в слово длинное, выводить только первые 10 букв в слове.
text = (input('введите текст используя пробел: '))
text = text.split() #    разделитель являеться пробел
# # if text.count() > 10:
# # print(text.count())
# arr = text.split()
# print(len(arr))
# print(*[f'{text} = {len(text)}\n' for text in arr])
# print(len(text))
for key, value in enumerate(text, 1):     # вернет кортеж потом распакует. enumerate-подсчитывает элементы
    print(f"{key} - {value}")
#использовать len ограничение длины вводимых строк