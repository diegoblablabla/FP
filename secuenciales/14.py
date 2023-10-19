numeros = []
for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

numeros.sort(reverse=True)

tres_mayores = numeros[:3]

promedio = sum(tres_mayores) / 3

print(f"Los 3 números son: {tres_mayores}")
print(f"El promedio de los 3 números es: {promedio:.2f}")
