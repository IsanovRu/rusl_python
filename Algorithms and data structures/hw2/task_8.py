# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def count(f, s):
    if not s:
        return 0
    elif f == s[0]:
        return 1 + count(f, s[1:])
    else:
        return 0 + count(f, s[1:])
с = count(str(input("введите число: ")),str(input("введите цифры: ")))
print(f'количество цифр в числе встречаются {с}')
