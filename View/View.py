from Model.Calculator import *

def view():
    flag = True
    while(flag):
        inData = input("Введите операцию: \n")
        if inData == "exit":
            flag = False
            break
        if len(inData) == 3:
            a, oper, b = tuple(inData)
        else:
            try:
               a, oper, b = tuple(inData.split())
            except:
                logging.error(f"Ошибка ввода: {inData}")
        calculator = Calculator(a, oper, b)
        print(f"Ответ: {calculator.run()} \n Введите exit для выхода")