import math
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

x, y = symbols('x y')

print('''Bienvenido
Al programa que resuelve ecuaciones diferenciales ''')

cat=''
while cat!='asdasdasf':
    try:
        cat=input('''
1. Asignar pista
2. Fin de programa
Ingrese la funcion que desea usar:  ''')
    except:
        print("Ingrese un valor Valido")
        cat=input('''
1. Asignar pista
2. Fin de programa
Ingrese la funcion que desea usar:  ''')
    if cat=='2':
        print("")
        print("Gracias por hacer uso del programa")
        break
    if cat=='1':
        
        exp1 = input("Ingrese la ecuacion que quiere resolver: ")
        while True:
            try:
                exp = parse_expr(exp1)
                break
            except:
                print("Ingrese Un valor Valido")
                #exp1 = input("Ingrese la ecuacion que quiere resolver: ")
        while True:
            try:
                paso = float(input("Ingrese el tamaño de paso: "))
                break
            except:
                print("Ingrese Un valor Valido")
                #paso = float(input("Ingrese el tamaño de paso: "))
        while True:
            try:
                x0 = float(input("Ingrese el valor inicial de x: "))
                break
            except:
                print("Ingrese Un valor Valido")
                #x0 = float(input("Ingrese el valor inicial de x: "))
        while True:
            try:
                y0 = float(input("Ingrese el valor inicial de y: "))
                break
            except:
                print("Ingrese Un valor Valido")
                #y0 = float(input("Ingrese el valor inicial de y: "))

        

        count = 0
        while count <6:
            try:
                res_exp = exp.subs([(x, x0), (y, y0)])
            except:
                print("Ingrese una funcion valida")
            y0 += (paso)*res_exp 
            x0 += paso 
            count = count + 1;
            print("%s. " %count)
            print("y = %s" %y0)
            print("x = %s" %x0)
    else:
        print("")
        print("Ingrese un valor Valido")
        print("")
            
            


