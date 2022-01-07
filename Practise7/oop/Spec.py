import Bonus as b
class Man:
    # fio = "Иван"
    def __init__(self,name,year,payment):
        self.name = name
        self.year = year
        self.payment = payment
        self.profession = 'Программист'

    def get_age(self):
        return 2021 - self.year
    def show_info(self):
        bonus = b.Bonus()#объект внешнего класса
        bonus.add_bonus(self)
        print(f"Добрый день, {self.name}. Ваш возраст: {self.get_age()}, профессия: {self.profession};оклад: {self.payment}")
