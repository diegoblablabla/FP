import os
os.system("cls")

p1_25 = 27
p26_50 = 25
p51mas= 23

unidades = int(input("cantidad de unidades: "))

if unidades >= 1 and unidades <= 25:
    importe = unidades * p1_25
if unidades >= 26 and unidades <= 50:
    importe = unidades * p26_50
if unidades >= 51  :
    importe = unidades * p51mas
print(f" compra : s/{importe:.2f}")