import random
from Order import *
from CarShowRoom import *

marki = ["Audi", "Skoda", "VW", "Porshe", "Lotus", "Volva", "Reno", "Mercedes", "Niva", "Toyota", "Mitsubishu", "Suzuki", "Akura"]

def f():
    car_brands = check_brands()
    title_factory = input("Введите наименование завода: ")
    title_car_showroom = input("Введите наименование автосалона: ")
    city = input("Введите наименование города: ")
    order = Order(CarShowRoom(title_car_showroom, city, title_factory, car_brands, random.randint(10, 30)))

def check_brands():
    while True:
        print(f"Список возможных брендов {marki}")
        car_brands = input("Введите бренды машин: ").split(" ")
        try:
            for brand in car_brands:
                if brand not in marki:
                    raise Exception(f"Нет такого бренда как {brand}! Повторите процедуру")
        except Exception as message:
                print(message)
                continue
        break
    return car_brands

if __name__ == '__main__':
    f()