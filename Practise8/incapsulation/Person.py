class Person:

    def __init__(self, fio, year):
        # private fileds __
        self.__fio = fio
        self.__year = year

    # Getters and Setters


    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.__fio = fio

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year in(1900, 2022):
            self.__year = year

    def show(self):
        print(f'{self.__fio} born in {self.__year}')


man = Person("Petrov", 1992)
print(man.year)