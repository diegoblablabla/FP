import os, math
os.system("cls")

altura = int(input("altura: "))
radio  = int(input("radio: "))

area = 2 * math.pi * radio * ( radio + altura)
volumen = math.pi * radio ** 2 * altura

print( f"area = {area:.2f}" )
print(f"volumen= {volumen:.2f}" )