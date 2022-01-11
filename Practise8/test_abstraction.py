from abc import ABC, abstractmethod

class MyAbstract(ABC):

    def test(self):
        print("testing methond not abstract")

    @abstractmethod
    def my_method(self):
        pass


class ClassM(MyAbstract):

    def my_method(self):
        print("Method 1")

t = ClassM()

t.my_method()
t.test()