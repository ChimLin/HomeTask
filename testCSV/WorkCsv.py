import csv
from random import randint
lst = [["Ivanov"], ["Arhipenkü"], ["Kulich"], ["Gronik"], ["Vakuha"]]

for x in lst:
    age = randint(18, 100)
    wage = randint(15000, 100000)
    x.append(age)
    x.append(wage)

print(lst)

file = open("persons.csv", "w")

for i in lst:
    s = i[0] + "," + str(i[1]) + "," + str(i[2])
    file.write(s + '\n')

file = open("persons.csv", "r")
# fio = input("age of emploeyy")
# for row in file:
#     if fio in row:
#         print(fio)


reader_csv = csv.reader(file)
s = list(reader_csv)
index = 0
wage = 0
for x in s:
    if wage < int(x[2]):
        wage = int(x[2])
        index = s.index(x)
print(s[index])

file.close()