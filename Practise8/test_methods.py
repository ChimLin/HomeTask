class MyClass:

    x = 10

    def __init__(self, name):
        self.__sos = name


    @classmethod
    def test(cls):
        print(f"{cls.x}, {cls.my_method(cls.x)}, {cls.usually(cls)}, {cls.test_static()}")

    @staticmethod
    def test_static():
        return "test"

    def usually(self):
        return "usually"

    @classmethod
    def my_method(cls, param):
        print(cls, param)

MyClass.test()

c = MyClass("name")