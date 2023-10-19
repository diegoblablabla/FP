import os, math
os.system("cls")

radio = int(input("radio: "))
altura = int(input("altura: "))

area_base = math.pi * (radio ** 2)
area_lateral = 2 * math.pi * radio * altura
area_total = 2 * area_base * area_lateral


print(f"area base = {area_base:.2f}")
print(f"area lateral = {area_lateral:.2f}")
print(f"area total = {area_total:.2f}")