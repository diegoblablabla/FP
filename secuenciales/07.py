import os
os.system("cls")

base = int(input("base: "))
altura = int(input("altura: "))

area = base * altura    
perimetro = 2* (base * altura)

print(f"area = {area:.2f}")
print(f"perimetro = {perimetro:.2f}")