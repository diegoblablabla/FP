import os
os.system("cls")

pies     = int(input("pies: ") )
pulgadas = int(input("pulgadas: ") )

metros = (pies * 12 + pulgadas) * 2.54 / 100

print( f"metros = {metros:.2f}" )