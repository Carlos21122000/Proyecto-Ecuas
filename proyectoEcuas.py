import math


y_ini = 1
x_ini = 1

y = y_ini
x = x_ini
count = 0
#dy/dx = y^2/x^3
while count <6:
    y += (0.5)*(y**2)/(x**3)
    x += 0.5;
    count = count + 1;
    print("%s. " %count)
    print("y = %s" %y)
    print("x = %s" %x)
