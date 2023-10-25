import os
os.system("cls")

dividendo = int(input("dividendo: "))
divisor = int(input("divisor: "))

cociente = 0
while dividendo >= divisor:
    dividendo -= divisor
    cociente += 1
    
print(f"cociente: {cociente}")
print(f"dividendo: {dividendo}")