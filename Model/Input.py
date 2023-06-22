from src.Operations import *
import logging

def inputData(a,oper,b):
    operation = Operations(a,b)
    if oper == "+":
        logging.info(f"Операция сложения")
        operation = Add(a,b)
    elif oper == "/":
        logging.info(f"Операция деления")
        operation = Division(a,b)
    elif oper == "*":
        logging.info(f"Операция умножения")
        operation = Multiplication(a,b)
    else:
        logging.error(f"Оператор {oper} не определен")
        return "Такой операции нет"
    return round(operation.oper(),4)
