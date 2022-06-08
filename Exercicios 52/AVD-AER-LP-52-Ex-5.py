y=str(input("Digite um número: "))
x=0
z=""
for i in range(0,len(y)):
    d=(y[x:x+1])
    x=x+1
    if d == "0":
        e="1"
        z=z+e
    
    if d == "1":
        e="2"
        z=z+e

    if d == "2":
        e="3"
        z=z+e

    if d == "3":
        e="4"
        z=z+e

    if d == "4":
        e="5"
        z=z+e

    if d == "5":
        e="6"
        z=z+e

    if d == "6":
        e="7"
        z=z+e

    if d == "7":
        e="8"
        z=z+e

    if d == "8":
        e="9"
        z=z+e

    if d == "9":
        e="0"
        z=z+e

print(z)