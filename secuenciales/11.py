import os
os.system("cls")

numero1 = input("Ingrese el primer numero: ")
numero2 = input("Ingrese el segundo numero: ")

if len(numero1) == 3 and len(numero2) == 3 and numero1.isdigit() and numero2.isdigit():
    numero1_nuevo = numero1[2] + numero1[1] + numero1[0]
    numero2_nuevo = numero2[2] + numero2[1] + numero2[0]

    print(f"El primer número es: {numero1_nuevo}")
    print(f"El segundo número es: {numero2_nuevo}")
else:
    print("Los numeros deben tener 3 digitos :)")
