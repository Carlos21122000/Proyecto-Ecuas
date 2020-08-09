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
fig, axes = plt.subplots()
axes.plot(x,sol,'--')
fig, axes = plt.subplots()
axes.plot(x,exacta(x))
plt.show()