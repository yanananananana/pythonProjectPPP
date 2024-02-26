with open("space.txt", encoding="utf-8") as file:
    # Преобразовать reader к списку
    data = list(file)
for i in range(len(data)):
    data[i] = data[i].split("*")
    if i + 1 != len(data):
        data[i][-1] = data[i][-1][:-1]
hash = dict()
c = 1
for i in range()