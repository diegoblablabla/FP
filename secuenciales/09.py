import os
os.system("cls")

numero = int(input("numero de 4 cifras: "))

if 1000 <= numero <= 9999 :
    cifra_1 = numero // 1000
    cifra_2 = (numero // 100) % 10
    cifra_3 = 12(numero // 10) %10
    cifra_4 = numero % 10
    
    cifra_total = cifra_1 + cifra_2 + cifra_3 + cifra_4
    
    print(f"la suma de las cifras = {cifra_total:.2f}")
