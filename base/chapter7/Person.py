# 人类
class Person:
    """
    人类
    """

    def __init__(self):
        self.__name = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def greet(self):
        print("Hello, world! I'm {}.".format(self.__name))


p = Person()
p.set_name("vvv")
p.greet()
