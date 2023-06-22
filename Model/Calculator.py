from Model.Input import inputData


class Model():
    def __init__(self, a, oper, b):
        self.a = a
        self.oper = oper
        self.b = b
class Calculator(Model):

    def run(self):
        if (self.a).isdigit() and (self.b).isdigit():
            return inputData(self.a, self.oper, self.b)
        else: return "Введенные данные не являются числами"
