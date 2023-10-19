import os, math
os.system("cls")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

discriminante = b**2 - 4*a*c

if discriminante > 0:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"Las soluciones son x1 = {x1} y x2 = {x2}")
elif discriminante == 0:
    x1 = -b / (2*a)
    print(f"La solución es x = {x1}")
else:
    print("no tiene solucion.")
