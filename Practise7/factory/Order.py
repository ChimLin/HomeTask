import random
import pymysql.cursors
from Factory import *
from CarShowRoom import *

class Order:

    def __init__(self, car_showroom: CarShowRoom):
        self.title_factory = car_showroom.title_factory
        self.cars = []
        self.dict = {}
        self.price_order = 0
        self.create_order(car_showroom.count_cars, car_showroom.marki)
        self.count_marki(car_showroom.marki)
        self.show()
        self.insert_into_tables(car_showroom)

    def show(self):
        print(f"Информация о заказе:\n")
        for car in self.cars:
            print(f"Автомобиль {car.name} стоит {car.price}\n")

        for label, number in self.dict.items():
            n = "раза" if number > 1 else "раз"
            print(f"Автомобиль марки {label} заказен {number} {n}\n")
        print(f"Сумма заказа: {self.price_order}")


    def count_marki(self, marki):
        for label in self.cars:
            if label.name in self.dict:
                self.dict[label.name] += 1
            else:
                self.dict[label.name] = 1

    def create_order(self, count_cars, marki):
        factory = Factory(self.title_factory)
        for i in range(1,count_cars):
            car = factory.create_car(marki[random.randint(0, len(marki) - 1)])
            self.cars.append(car)
            self.price_order += car.price

    def connect_db(self):
        try:
            connect = pymysql.connect(host="localhost",
                                      user='root', password='',
                                      db='cars',
                                      cursorclass=pymysql.cursors.DictCursor)
        except Exception as message:
            print(message)
        return connect

    def insert_into_tables(self, showroom):
        connect = self.connect_db()
        with connect:
            cur = connect.cursor()
            try:
                cur.execute(f"INSERT INTO car_showroom(title_car_showroom, city) VALUES ('{showroom.title}', '{showroom.city}')")
                id_showroom = int(cur.lastrowid)
                print(self.price_order, showroom.count_cars, id_showroom)
                #cur.execute("INSERT INTO order(factory, sum, count_cars, id_showroom) VALUES ('{factory_name}', {sum_order}, {counts}, {id_show})".format(factory_name = showroom.title_factory, sum_order = self.price_order, counts = showroom.count_cars, id_show = id_showroom))

                for car in self.cars:
                    cur.execute("INSERT INTO car(name, price, id_order, id_showroom) VALUES  ('{name}', {price}, {id_order}, {id})".format(name = car.name, price = car.price, id_order = id_showroom, id = id_showroom))
                connect.commit()

            except Exception as message:
                print(message)
                connect.rollback()


