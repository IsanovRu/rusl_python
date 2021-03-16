# Реализовать функцию int_func(), принимающую слова
# из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например,
# print(int_func(‘text’)) -> Text.
def int_func(*args):
    res = ''
    for arg in args:
        res += ' '+arg.strip().capitalize() # можно наращивать много функции
    return res
print(int_func('text'))
print(int_func(str(input("Введите текст -"))))
