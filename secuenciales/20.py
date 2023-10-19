import os
os.system("cls")

cantidad_soles = float(input("dinero: "))
billetes_monedas = [200, 100, 50, 20, 10, 5, 2, 1]
cantidad_billetes_monedas = []

for denominacion in billetes_monedas:
    cantidad = cantidad_soles // denominacion
    cantidad_billetes_monedas.append(cantidad)
    cantidad_soles %= denominacion

print("descomposicion de dinero:")
for i in range(len(billetes_monedas)):
    if cantidad_billetes_monedas[i] > 0:
        if billetes_monedas[i] >= 5:
            print(f"{cantidad_billetes_monedas[i]} billetes de {billetes_monedas[i]} soles")
        else:
            print(f"{cantidad_billetes_monedas[i]} monedas de {billetes_monedas[i]} soles")
