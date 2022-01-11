from Practise8.inheritance.Car import Car

class RaceCar (Car):

    def __init__(self, title, price, speed):

        #super(self, title, price)
        Car.__init__(self, title, price)
        self.__speed = speed


    def info(self):
        print(super().info())
        self.title()
        print(f'{self.__title} spuedd up to {self.__speed}')


re = RaceCar("Porshe", 5567, 25666)
re.info()