import os
os.system("cls")

capital_juan = float(input("capital Juan en dólares: "))
capital_rosa = float(input("capital Rosa en dólares: "))
capital_daniel = float(input("capital de  Daniel en soles: "))

capital_total_dolares = capital_juan + capital_rosa + (capital_daniel / 3.00)

porcentaje_juan = (capital_juan / capital_total_dolares) * 100
porcentaje_rosa = (capital_rosa / capital_total_dolares) * 100
porcentaje_daniel = (capital_daniel / 3.00 / capital_total_dolares) * 100

print(f"El capital total en dólares es: ${capital_total_dolares:.2f}")
print(f"porcentaje de Juan {porcentaje_juan:.2f}%.")
print(f"porcentaje de Rosa {porcentaje_rosa:.2f}%.")
print(f"porcentaje de Daniel {porcentaje_daniel:.2f}%.")
