import os
os.system("cls")

numero = int(input("ingresar numero de 4 cifras: "))

if 1000 <= numero <= 9999 :
    cifra_1 = numero % 10
    cifra_2 = (numero // 10) % 10
    cifra_3 = (numero // 100) % 10
    cifra_4 = numero // 1000
    
    cifra_final = (cifra_1 * 1000) + (cifra_2 * 100) + (cifra_3 * 10) + cifra_4
    
    print(f"numero final :{cifra_final}")