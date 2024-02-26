"""
Решение задачи 2 предпрофессионального экзамена.
Программа читает файл данных, сортирует данные по номеру корабля в порядке возрастания и вывеодит 10 первых кораблей в получившемся списке.
"""
with open("space.txt", encoding="utf-8") as file:
    # Преобразовать reader к списку
    data = list(file)
    # Строка с подписями столбцов
for i in range(len(data)):
    data[i] = data[i].split("*")
    if i + 1 != len(data):
        data[i][-1] = data[i][:-1]
    if i > 0:
        data[i][0] = data[i][0].split("-")
headlines = data.pop(0)
for i in range(len(data)):
    for j in range(len(data) - 1):
        if int(data[j][0][1]) < int(data[j + 1][0][1]):
            data[j], data[j + 1] = data[j + 1], data[j]
for i in range(10):
    print(data[i][0][0] + "-" + data[i][0][1])
