from abc import ABC, abstractmethod

"""Есть базовый класс Товар с основными свойствами, присущими всем товарам.
Есть класс Цифровой, штучный и товар на вес. У товара цифрового цена постоянная и связана с ценой штучного товара, 
у штучного товара цена в 2 раза выше чем у цифрового. У каждого товара должен быть метод для нахождения общей стоимости
товара, а также метод для получения прибыли от продажи товара
"""
class Item(ABC):

    price = 0
    title = ""
    type = ""
    weight = 0
    count = 0
    spent_money = 0

    @abstractmethod
    def total_price(self):
        pass

    @abstractmethod
    def benefit(self):
        pass

class OneItem(Item):

    def __init__(self, price, title, type, weight, count, spent_money):
        self.spent_money = spent_money
        self.price = price
        self.title = title
        self.type = type
        self.weight = weight
        self.count = count

    def total_price(self):
        return self.price  * 2 * self.count

    def benefit(self):
        print(f"Чистая прибыли составляет: {self.total_price() - self.spent_money}")

class DigitItem(Item):

    def __init__(self, one_item: OneItem):
        self.price = one_item.price
        self.title = one_item.title
        self.type = one_item.type
        self.weight = one_item.weight
        self.count = one_item.count
        self.spent_money = one_item.spent_money


    def total_price(self):
        return self.count * self.price

    def benefit(self):
        print(f"Чистая прибыли составляет: {self.total_price() - self.spent_money}")

oneItem = OneItem(1000, "Milk", "Milky product", 6000, 400, 10000)
print(oneItem.total_price())
oneItem.benefit()

digitItem = DigitItem(oneItem)
print(digitItem.total_price())
digitItem.benefit()