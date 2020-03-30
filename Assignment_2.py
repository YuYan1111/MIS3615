import match

print("Quadratic function: ax**2+bx+c=0")

#Coefficient
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

def quadratic(a, b, c):
Discriminant = b**2 - 4*a*c

    if Discriminant >= 0:
        x1 = (((-b) + math.sqrt(Discriminant))/(2*a))
        x2 = (((-b) - math.sqrt(Discriminant))/(2*a))
        return x_1, x_2
    else:
        return None, None
    def main()
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
    
    sol_1,sol_2 = quadratic(a,b,d)
    if sol_1:
        print(f"The roots of the equation are (sol_1) and (Sol_2).")
    else:
        print("No real number soution")

    if _name_ =="__main__":
        main()
