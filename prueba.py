# solucion ecuaciones diferenciales de primer orden
# https://www.youtube.com/watch?v=LbcjNGE5gkM
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(y,x):
    return (x**2)*(1+y)
def exacta(x):
    return 4*(np.exp(x**3/3))-1
    
y0=3.0
x=np.linspace(0,1,100)

sol = integrate.odeint(f,y0,x)

#print(sol)
# grafica solucion numerica
def graficarSolNumerica(x,sol):
    fig, axes = plt.subplots()
    plt.title("Solucion Numerica")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    axes.plot(x,sol,'--')
    return plt.show()
    


# grafica solucion exacta
def graficarSolExacta(x):
    fig, axes = plt.subplots()
    plt.title("Solucion Exacta")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    axes.plot(x,exacta(x))
    return plt.show()
    
    
    
graficarSolExacta(x)
graficarSolNumerica(x,sol)