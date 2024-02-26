from csv import writer, reader
def gen(i):
    password = info[1][-3:]
    password = password + info[0][2] + info[0][1]
    password = password + info[1][2] + info[1][1] + data
    password = password.upper()
    return password

with open("space.txt", uncoding = "utf-8") as file:
    data = list(file)
for i in range(len(data)):
    data[i] = data[i].split("*")
    if i + 1 != len(data):
        data[i][-1] = data[i][-1][:-1]
data[0].append("password")
for i in range(1,len(data)):
    data[i].append(gen(data[i])
with open("space_uniq_password.csv", "w",uncoding = "utf-8") as file:
    writing = writer(file, delimiter=";")
    writing.writerows(data)
file.close()