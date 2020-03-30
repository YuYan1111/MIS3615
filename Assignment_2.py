
from math import sqrt

print("Quadratic function: ax**2+bx+c=0")

#Coefficient
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

#Discriminant
d = (b**2) - (4*a*c)

def quadratic(a, b, c):
    if d > 0:
        discriminant = 2
        x1 = (((-b) + sqrt(d))/(2*a))
        x2 = (((-b) - sqrt(d))/(2*a))
        return("The answers are {} and {}" .format(x1, x2))
    elif d == 0:
        discriminant = 1
        x = (-b)/(2*a)
        return("The answer is {}" .format(x))
    else:
        discriminant = 0
        return("No answer")

print(quadratic(a, b, c))
