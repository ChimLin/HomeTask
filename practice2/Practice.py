total = 0

# for i in range(0, 5):
#     num = int(input("Введите число: "))
#     answer = input("Данные число учитывать при суммровании? (y/n)")
#     if answer == "y":
#         total += num
#
# print(total)

# function
outer = 3
def print_sum(a = 0, b = 0):
    a + b + outer
    return
a = print_sum(3, b = 3)

def is_even(n):
    return n % 2 == 0

def calc(a, b):
    if(not is_even(a) and is_even(b)):
        return a + b
    return a * b

print(calc(2,8))

#Lambda expression
# Анонимные функции
func = lambda a,b: a + b
print(func(3,4))

# влоденные функции

def outer_func(n):
    def inner_func(x):
        return  x + n

    def size_disk(x):
        print(n, x, "dfd, ", sep=" ")
    return inner_func
test = outer_func(5)
print(test(4))#


#global var

def hell(f):
    global name
    name = "g"
    print("Hi", f)

print(hell("sdfd"))
print(name)

# def sum(a, b, *x):
#     print(type(x))
#     for n in x:
#         print(n)
#
# sum(1,2,3,4,5,6)

# recursion
# def rec(b):
#     if b == - 1:
#         return b
#     print(b)
#     rec(b - 1)
#
# rec(5) # для дерева

def power(a,n):
    if n == 1:
        return a
    return a * power(a, n - 1)

print(power(3, 2))

#list

numbers = [10,20,30,40,50]
numbers2 = list(numbers)
print(numbers2)

lst =[1] * 5
print(lst)

print(type(range(5, 10, 2)))

li = list(range(1,100,4))
print(li)


# compare 2 lists

list_1 = [1,2,3,4,5]
list_2 = list(range(1,6))

print(list_1 == list_2)

# add element in list


ll = ["one", "two", "three"]


def find_max_elem(lst):
    element = lst[0]
    for x in lst[1:]:
        if x > element:
            element = x
    return element


print(find_max_elem([-6,-5,-4,3,4]))



def change(lst):
    element = lst[0]
    lst[0] = lst[-1]
    lst[-1] = element
    return lst

s = [1,2,3]
print(change(ll))

def print_odd_lst(lst):

    lst = [item for item in lst if item % 2 != 0]
    print(lst)

s21 = [1,2,3]
s22 = (1,2,3)

print(s21.__sizeof__())
print(s22.__sizeof__())

print(isinstance((1,2), tuple))

#dit

ab = [
    ["a",123],
    ["b", 123],
    ["c", 1233],
]

new_ab = dict(ab)

print((new_ab))
for key, value in new_ab.items():
    print(key, value)

print('Hello man asdf \rWorld!')

str = input().split(" ")
print(" ".join(list(reversed(str))))

"a".startswith()