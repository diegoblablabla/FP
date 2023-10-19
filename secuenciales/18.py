import os
os.system("cls")

cantidad = int(input("cantidad de unidades: "))
precio_unitario = float(input("precio unitario del artículo: "))

importe_compra = cantidad * precio_unitario
primer_descuento = importe_compra * 0.15
importe_con_primer_descuento = importe_compra - primer_descuento
segundo_descuento = importe_con_primer_descuento * 0.15
importe_a_pagar = importe_con_primer_descuento - segundo_descuento

print(f"Importe de la compra sin descuento: {importe_compra:.2f}")
print(f"Primer descuento 15%: {primer_descuento:.2f}")
print(f"Importe con el primer descuento: {importe_con_primer_descuento:.2f}")
print(f"Segundo descuento (15% sobre el importe con el primer descuento): {segundo_descuento:.2f}")
print(f"Importe a pagar: s/. {importe_a_pagar:.2f}")
