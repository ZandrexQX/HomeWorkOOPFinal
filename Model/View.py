from Model.Calculator import *

def view():
    flag = True
    while(flag):
        inData = input("Введите операцию: ")
        if inData == "exit":
            flag = False
            break
        if len(inData) == 3:
            a, oper, b = tuple(inData)
        else:
            a, oper, b = tuple(inData.split())
        calculator = Calculator(a, oper, b)
        print(f"Ответ: {calculator.run()} \n Введите exit для выхода")