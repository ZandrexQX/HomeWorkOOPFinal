from src.Operations import *

def inputData(a,oper,b):
    operation = Operations(a,b)
    if oper == "+":
        operation = Add(a,b)
    elif oper == "/":
        operation = Division(a,b)
    elif oper == "*":
        operation = Multiplication(a,b)
    else: return "Такой операции нет"
    return operation.oper()
