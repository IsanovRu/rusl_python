# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
try:
    with open("hw3.txt", "r") as f_obj:  #Читаем файл
         lines = f_obj.read().splitlines() # read().splitlines() - чтобы небыло пустых строк
         dic = {} # Создаем пустой словарь
         for line in lines: # Проходимся по каждой строчке
             key,value = line.split(' - ')  # Разделяем каждую строку по двоеточии(в key будет - имена, в value - цена)
             dic.update({key: value})	 # Добавляем в словарь
         print(dic)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f_obj.close()
print('количество слов в файле - ', len(set(open("hw3.txt").read().split())))

# решение преподавателя  ver.1
with open('3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')

# решение преподавателя  ver.2
with open('3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    # используя генератор ключей line.split()[0]: перебираем for line in f получаем строку далее делаем split
    # с ключем [0]имя во float преобразуем зарплату float(line.split()[1] ИТОГО Получаем СЛОВАРЬ С сотрудниками
    #
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')