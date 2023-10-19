import os
os.system("cls")

monto_donacion = float(input("Ingrese la donación anual: "))

monto_centro_salud = monto_donacion * 0.25
monto_comedor_infantil = monto_donacion * 0.35
monto_escuela_infantil = monto_donacion * 0.25
monto_asilo_ancianos = monto_donacion * 0.15  

print(f"Monto asignado al Centro de Salud: ${monto_centro_salud:.2f}")
print(f"Monto asignado al Comedor Infantil: ${monto_comedor_infantil:.2f}")
print(f"Monto asignado a la Escuela Infantil: ${monto_escuela_infantil:.2f}")
print(f"Monto asignado al Asilo de Ancianos: ${monto_asilo_ancianos:.2f}")
