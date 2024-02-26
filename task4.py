"""
Решение задачи 4 предпрофессионального экзамена.
Программа читает файл с данными, для каждого корабля генерирует слово-пароль.
Новые данные сохраняются в файл csv.
В программе реализованы функции:
generate_password - для генерации пароля по установленным правилам
"""
from csv import writer, reader


def generate_password(i):
    password = info[1][-3:]
    password = password + info[0][2] + info[0][1]
    password = password + info[1][2] + info[1][1] + data
    password = password.upper()
    return password


with open("space.txt", encoding="utf-8") as file:
    # Преобразовать reader к списку
    data = list(file)
for i in range(len(data)):
    data[i] = data[i].split("*")
    if i + 1 != len(data):
        data[i][-1] = data[i][-1][:-1]
data[0].append("password")
for i in range(1, len(data)):
    data[i].append(generate_password(data[i])
    with open("space_uniq_password.csv", "w", encoding="utf-8") as file:
        writing = writer(file, delimiter=";")
    writing.writerows(data)
    file.close()
