import os
os.system("cls")

tarifa_horaria = float(input("Ingrese la tarifa horaria: "))
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))

sueldo_basico = tarifa_horaria * horas_trabajadas

bonificacion = sueldo_basico * 0.20
sueldo_bruto = sueldo_basico + bonificacion

descuento = sueldo_bruto * 0.10
sueldo_neto = sueldo_bruto - descuento

print(f"Sueldo Básico: ${sueldo_basico:.2f}")
print(f"Sueldo Bruto: ${sueldo_bruto:.2f}")
print(f"Sueldo Neto: ${sueldo_neto:.2f}")
