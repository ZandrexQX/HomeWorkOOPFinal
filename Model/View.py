from Model.Calculator import *

a, oper, b = tuple(input())
calculator = Calculator(a, oper, b)

print(calculator.run())