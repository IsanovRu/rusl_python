# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
def number_():
    try:
        n = int(input("введите любый числа посчитает сколько четны и нечетных: "))
        even=odd=0
        while n>0:
            if n%2 == 0:
              even += 1
            else:
              odd += 1
            n = n//10
        print("четных - %d, нечетных - %d" % (even, odd))
    except Exception:   print("Вы ввели не числа. Введите числа: ")
number_()
