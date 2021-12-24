#read file

with open("test.txt", "r") as file:
    for line in file:
        print(line)

matrix = [
    [2,3,4],
    [5,6,7],
    [3,2,6]
]

# 1) Сохранить матрицу в файле
# 2) Считыаем матрицу из файла и выводим в консоль элементы матрицы таким образом, чтобы каждый элемент был возведен в степень
# равную номеру строки, в которой он находится

file = open('matrix1.txt','w')
i = 0
while i < len(matrix):
    j = 0
    s = ''
    while j < len(matrix[i]):
        s += str(matrix[i][j]) + ' '
        j += 1
    file.write(s + '\n')
    i += 1
file.close()

with open('matrix1.txt','r') as file:
    number_row = 1
    for line in file:
        mas = line.split(' ')
        for item in mas:
            if item != '\n':
                print(int(item) ** number_row, end=' ')
        print()
        number_row +=1


# 2) Сделать отдельный столец и строку, где вычисляем сумму по строкам и столбцам
print("--------------------------------")

def find_sum_of_row(text):
    sum_of_row = 0
    lst = line.split(" ")
    new_lst = []
    for item in lst:
        if item != '\n':
            sum_of_row += int(item)
            new_lst.append(int(item))
    new_lst.append(sum_of_row)
    return new_lst

def add_new_numbers_rows(matrix):
    file = open('matrix1.txt', 'w')
    i = 0
    while i < len(matrix):
        j = 0
        s = ''
        while j < len(matrix[i]):
            s += str(matrix[i][j]) + ' '
            j += 1
        file.write(s + '\n')
        i += 1
    file.close()

def add_sum_column_rows(lst):
    file = open("matrix1.txt", "a")
    for x in lst:
        file.write(str(x) + " ")
    file.write('\n')
    file.close()

def sum_lists(lst1, lst2):
    sum_list = []
    for (item1, item2) in zip(lst1, lst2):
        sum_list.append(item1 + item2)
    return sum_list

sum_new_rows = []
sum_new_columns = []

with open('matrix1.txt','r') as file:
    for line in file:
        sum_new_rows.append(find_sum_of_row(line))
    sum_new_columns = [0] * len(sum_new_rows[0])
    for lst in sum_new_rows:
        sum_new_columns = sum_lists(lst, sum_new_columns)

add_new_numbers_rows(sum_new_rows)
add_sum_column_rows(sum_new_columns)


