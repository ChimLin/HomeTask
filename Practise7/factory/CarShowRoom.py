import itertools

class CarShowRoom:

   # id_iter = itertools.count()

    def __init__(self, title, city,  title_factory, marki, count_cars):
        #self.id = next(CarShowRoom.id_iter)
        self.title = title
        self.city = city
        self.title_factory = title_factory
        self.marki = marki
        self.count_cars = count_cars

   # def get_id(self):
        #return self.id

    def get_title_factory(self):
        return self.title_factory

    def get_title(self):
        return self.title

    def get_city(self):
        return self.city

    def get_marki(self):
        return self.marki

    def get_count_cars(self):
        return self.count_cars


