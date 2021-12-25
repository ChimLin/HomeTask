# try:
#     raise ZeroDivisionError("eror")
# except ZeroDivisionError:
#     print(ZeroDivisionError.args)
# else:
#     print("no")
# finally:
#     print("noNO")
#
# a = 0
# b = 0
#
# assert a != 0, "Не ноль"
# print("resilt", a / b)

try:
    raise Exception("just exception")
except Exception as e:
    print(e)

lst1, lst2 = [1,2,3,4,5], [1,0,3,0,5]

for index in range(0, len(lst2)):
    try:
        lst1[index] / lst2[index]
    except Exception as message:
        print(message)



#
# while True:
#     first = input("first number")
#     if first == "q":
#         break
#     second = input("second number")
#     if first == "q":
#         break
#     try:
#         a = int(first) / int(second)
#     except ZeroDivisionError as message:
#         print(f"<fgd {message}")
#
#
