import os
os.system("cls")

#def multiplicar(x,y):
    #resultado = 0 
    #if y < 0 :
        #x,y = -x, -y
           
n1 = int(input("primer numero: "))
n2 = int(input("segundo numero: "))

rpt = 0
for i in range(abs(n2)):
        rpt += n1


print(f"resultado: {rpt}")