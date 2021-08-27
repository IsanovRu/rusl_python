# Для чисел в пределах от 20 до 240 найти числа,
# кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
# nums = list(range(20, 241))
print([n for n in range(20, 240+1, 20)])  # это без фильтра
print([n for n in range(20, 240+1, 21)])
print([n for n in range(20, 240+1) if n % 20 == 0 or n % 21 == 0])  # это с фильтром 20 и 21
