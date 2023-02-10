# Object oriented programming

class Employee:
    __name = None
    __id = 0
    __salary = 0

    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_id(self, ide):
        self.__id = ide

    def get_id(self):
        return self.__id

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


Kkhan = Employee("Kutbuddin", 420, 12000)
print(Kkhan.get_id())
# Kkhan.set_name('Kutbuddin khan')
print(Kkhan.get_name())
print(Kkhan.get_salary())
