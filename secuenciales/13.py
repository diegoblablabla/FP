import os, math
os.system("cls")

def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a**2 + cateto_b**2)

cateto_a = float(input("cateto1: "))
cateto_b = float(input("cateto2: "))

hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)

print(f"la hipotenusa= {hipotenusa}")
