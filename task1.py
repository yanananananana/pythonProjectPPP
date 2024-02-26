"""
Решение задачи 1 предпрофессионального экзамена.
Программа читает данные из txt-файла, ищет координаты
Затем по формуле считает приближенные к истине значения координат последнего места связи и заменяет ими нулевые результаты
и сохраняет в новый файл.
"""
from csv import writer, reader
with open('space.txt') as file:
    key = list(file)
for i in range(len(key)):
    key[i] = key[i].split('*')
    if i+1 != len(key):
        key[i][-1] = key[i][-1][:-1]

for i in range(len(key)):
    if key[i][2]=='0 0':
        name = key[i][0].split('-')
        dir = key[i][-1].split()
        print(name,dir)
        if int(name[1][0])>5:
            x = int(name[1][0]) + int(dir[0])
        else:
            x = -1 * (int(name[1][0])+int(dir[0])) * 4 + len(key[i][1])
        if int(name[1][1]) > 3:
            y = int(name[1][1]) + len(key[i][1]) + int(dir[1])
        else:
            y = -1 * (int(name[1][0]) + int(dir[1]) * int(name[1][1]))
        key[i][2] = f'{x}{y}'

file = open('space_new.txt', 'w', encoding = "utf-8")
for i in range(len(key)):
    add = ""
    for j in range(4):
        add += i[j]
        if j<3:
            add += "*"
        else:
            add += "\n"
    file.writelines(add)
file.close()

for i in top:
    coord = i[2].split()
    print(f'{i[0] - ({coord})}')
