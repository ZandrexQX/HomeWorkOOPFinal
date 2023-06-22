from Model.Calculator import *

def view():
    inData = input("Введите операцию: ")
    if len(inData) == 3:
        a, oper, b = tuple(inData)
    else:
        a, oper, b = tuple(inData.split())
        print(a)
        print(b)
        print(oper)
    calculator = Calculator(a, oper, b)
    print(f"Ответ: {round(calculator.run(),4)}")