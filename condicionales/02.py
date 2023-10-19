import os
os.system("cls")

precio = 20

productos = int(input("cantidad de producto: "))
cc = productos * precio

if cc > 700:
    descuento = 0.16
elif cc >= 501:
    descuento = 0.14
else:
    descuento = 0.12
    
descuentoT = cc * descuento
tpagar = cc - descuentoT

print(tpagar)