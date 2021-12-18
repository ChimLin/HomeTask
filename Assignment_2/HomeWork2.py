#1 Fibonnachi

def print_fibonachi(number):
    n1, n2 = 0, 1
    if number < 0:
        print("Введите положительное чсло")
    elif number == 1:
        print("Последовательность Фибоначчи", number, ":")
        print(n1)
    else:
        preceding_value = 0
        while preceding_value < number:
            print(n1, end= " ")
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            preceding_value += 1
    print()
print_fibonachi(100)

# 2 list

lst = ["Дзюдо", "Йога"]
lst.append(input("Ваш любимый спорт? "))
lst.sort()
print(lst)

#3 School
def remove_unlike_lesson(lst):
    lovely_classes = lst.copy()
    for x in lst:
        while True:
            answer = input("Нравится предмет {list_sc}? (y/n) ".format(list_sc=x))
            if answer == 'n':
                lovely_classes.remove(x)
                break
            elif answer == 'y':
                break
            else:
                print("Неверный ответ. Попробуйте еще раз")
                continue
    print("Ваши любимые предметы:", " ".join(lovely_classes))

lst_school = "Физика Алгебра Музыка География Химия Информатика".split(" ")
remove_unlike_lesson(lst_school)

#4

dishes = input("Введите ваши 4 любимые блюда: ").split(" ")

def print_content_dict(dct):
    for key, value in dct.items():
        print(key, ":" , value)

def del_element_by_value_keys(del_element, dct):
    if del_element.isnumeric():
        del dct[int(del_element)]
    else:
        for key, value in dct.items():
            if value == del_element:
                del dct[key]
                break


def del_dis(lst):
    dct = {}
    key = 1
    for x in lst:
        dct[key] = x
        key +=1
    print_content_dict(dct)
    del_element = input("Введите ключ или значение элемента для удаления: ")
    del_element_by_value_keys(del_element, dct)
    sorted_dct = dict(sorted(dct.items(), key= lambda kv: kv[1]))
    print_content_dict(sorted_dct)

del_dis(dishes)