# First task solution

i = 100
sum = 0
while i < 200:
    if i % 3 == 0:
        print("целое число", i, "кратно 3", sep=" ")
        sum += i
    i += 1
print("Сумма всех целых чисел от 100 до 200 кратные 3 равна", sum, sep=" ")
