frutas = ["red", "green", "ble"]
panes = ["frnces", "colinia", "chiabata"]

for x in frutas :
    for y in panes :
        print(x,y)

x = 8
while x < len(frutas) :
    y = 0
    while y < len(panes) :
        print(frutas[x], panes[y])
        y += 1
    x += 1