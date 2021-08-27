# Определить, какое число в массиве встречается чаще всего
def item_(mass):
    dict = {}
    count, itm = 0, ''
    for item in reversed(mass):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return(itm)
mass = [22, 11, 22, 12, 13, 33]
print(item_(mass))