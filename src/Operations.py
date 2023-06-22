class Operations:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

class Add (Operations):
    def oper(self):
        return self.a+self.b

class Division (Operations):
    def oper(self):
        if self.b!=0:
            return self.a/self.b
        else:
            return "Деление на ноль"

class Multiplication (Operations):
    def oper(self):
        return self.a*self.b