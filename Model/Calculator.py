from Model.Input import inputData
import logging

class Model():
    def __init__(self, a, oper, b):
        self.a = a
        self.oper = oper
        self.b = b
class Calculator(Model):

    def run(self):
        try:
            a1 = (float)(self.a)
            b1 = (float)(self.b)
            logging.info(f"Введено {a1} и {b1}")
        except:
            logging.error(f"Ошибка данных: {self.a} или {self.b}")
            return "Введенные данные неверны"
        return inputData(a1, self.oper, b1)
