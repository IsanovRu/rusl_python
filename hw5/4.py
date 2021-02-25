# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def hw4():
    dic = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
    }
    with open("4n.txt", "r",  encoding="utf-8") as fen:
        with open("4m.txt", "w",  encoding="utf-8") as frn:
            for str in fen:
                try:
                    datalist = str.split()
                    datalist[0] = dic.get(datalist[0], "Неразботчиво")
                    frn.write("{} {} {} \n".format(datalist[0], datalist[1], datalist[2]))
                except Exception as e:
                    print('Не могу считать/разобрать строку "{}". Пропускаю'.format(str))

with open('4m.txt', 'r', encoding='utf-8') as mf:
        text = mf.read()
        print(text)