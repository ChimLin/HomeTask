# class Auto:
#
#
#     @staticmethod
#     def get_class_info():
#         print("Info about class")
#
# Auto.get_class_info()

# class MyClass:
#
#     @staticmethod
#     def sum(a, b):
#         return a + b
#
#     @staticmethod
#     def div(a, b):
#         return a / b
#
#     @staticmethod
#     def mul(a, b):
#         return a * b
#
#     @staticmethod
#     def diff(a, b):
#         return a - b

class Bank:

    def __init__(self, money):
        self.money = money

    @staticmethod
    def profit(money, year, rate):
        return  year +(money * rate / 100)


class VTB(Bank):

    def __init__(self, balance):
        super().__init__(balance)

    @staticmethod
    def profit(money):
        return  money * 1.2

vtb = VTB(10000)
print(Bank.profit(vtb.money, 3.5,5))