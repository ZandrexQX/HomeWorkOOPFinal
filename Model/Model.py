from Model.Input import inputData


class Calculator():
    def __init__(self, a, oper, b):
        self.__a = a
        self.__oper = oper
        self.__b = b

    def run(self):
        if (self.__a).isdigit() and (self.__b).isdigit():
            return inputData(self.__a, self.__oper, self.__b)
        else: return "Введенные данные не являются числами"
