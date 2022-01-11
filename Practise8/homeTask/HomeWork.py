from abc import ABC, abstractmethod

class WorkerBase (ABC):

    def __init__(self, occupation, base_rate):
        self.occupation = occupation
        self.base_rate = base_rate

    def __str__(self):
        return f"Занятость: {self.occupation}. Базовая ставка {self.base_rate}"

    @abstractmethod
    def calculate_salary(self):
        pass

class Programmer(WorkerBase):



    def __init__(self, occupation, base_rate):
        super().__init__(occupation, base_rate)

    def calculate_salary(self):
        print(f"Заработная плата {self.occupation}: {4 * self.base_rate} у.e. \n")


class Economist(WorkerBase):


    def __init__(self, occupation, base_rate):
        super().__init__(occupation, base_rate)

    def calculate_salary(self):
        print(f"Заработная плата {self.occupation}: {2 * self.base_rate} у.e. \n")


class Manager(WorkerBase):


    def __init__(self, occupation, base_rate):
        super().__init__(occupation, base_rate)

    def calculate_salary(self):
        print(f"Заработная плата {self.occupation}: {10 * self.base_rate} у.e. \n")


programmer = Programmer("Programmer", 2000)
print(programmer.__str__())
programmer.calculate_salary()


economist = Economist("Economist", 2000)
print(economist.__str__())
economist.calculate_salary()

manager = Manager("Manager", 2000)
print(manager.__str__())
manager.calculate_salary()
