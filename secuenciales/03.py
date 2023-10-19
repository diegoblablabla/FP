import os
os.system("cls")

kilometros = int(input("kilometros: ") )
pies       = int(input("pies: ") )
millas     = int(input("millas: ") )

metros = kilometros * 1000 + pies / 3.2808 + millas * 1609
yardas = metros * 3.2808 / 3

print( f"metros = {metros:.2f}" )
print( f"yardas = {yardas:.2f}" )