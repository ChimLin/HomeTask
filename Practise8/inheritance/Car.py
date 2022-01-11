class Car:

    def __init__(self, title, price):
        self.__title = title
        self.__price = price

    def __test(self):
        print("Hey")

    @property
    def title(self):
        return self.__title

    @title.setter
    def fio(self, title):
        self.__title = title

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
         self.__price = price

    def info(self):
        return f"{self.__title} cost {self.__price}"


    def title(self):
        print("hey")
