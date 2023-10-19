import os
os.system("cls")

hombres = int(input("hombres: "))
mujeres = int(input("mujeres: "))

total_de_estudiantes = (hombres + mujeres)

porcentaje_hombres = ( hombres / total_de_estudiantes) * 100
porcentaje_mujeres = ( mujeres / total_de_estudiantes) * 100
print(f"porcentaje de hombres: {porcentaje_hombres:.2f}%") 
print(f"porcentaje de mujeres: {porcentaje_mujeres:.2f}%") 
