# Создать (не программно) текстовый файл, в котором каждая
# строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

import json


with open("firms.txt", "r",  encoding="utf-8") as f:
    psum = 0
    profit = {}
    loses = {}
    for str in f:
        try:
            datalist = str.split()
            name = datalist[0]
            delta = float(datalist[2])-float(datalist[3])
            if delta >= 0:
                psum += delta
                profit[name] = delta
            else:
                loses[name] = delta
        except Exception as e:
            print('Не могу считать/разобрать строку "{}". Пропускаю'.format(str))
    average = {'average_profit': psum/len(profit), }
    lst = [profit, average, loses]
    with open("firms.json", "w", encoding='utf-8') as jsonfile:
        json.dump(lst, jsonfile)

