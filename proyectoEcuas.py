import math
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

x, y = symbols('x y')


#dy/dx = y**2/x**3
exp1 = input("Ingrese la ecuacion que quiere resolver: ")
paso = float(input("Ingrese el tamaño de paso: "))
x0 = float(input("Ingrese el valor inicial de x: "))
y0 = float(input("Ingrese el valor inicial de y: "))

exp = parse_expr(exp1)

count = 0



while count <6:
    res_exp = exp.subs([(x, x0), (y, y0)])

    y0 += (paso)*res_exp 
    x0 += paso 
    count = count + 1;
    print("%s. " %count)
    print("y = %s" %y0)
    print("x = %s" %x0)


