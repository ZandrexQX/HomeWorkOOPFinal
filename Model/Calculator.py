from Model.Input import inputData


class Model():
    def __init__(self, a, oper, b):
        self.a = a
        self.oper = oper
        self.b = b
class Calculator(Model):

    def run(self):
        a1 = (float)(self.a)
        b1 = (float)(self.b)
        return inputData(a1, self.oper, b1)
