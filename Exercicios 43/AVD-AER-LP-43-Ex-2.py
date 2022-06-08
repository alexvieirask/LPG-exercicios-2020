contador=0
num=0
primeiro=True
div=0


while True:
    i=(input("Digite um numero: "))
    if i =="fim":
        break
    else:
        contador=contador+1
        i=float(i)
        num=num+i
        i=num
        div=num/contador
        primeiro=False

if primeiro:
    print("Você não digitou um numero!")
else:
    print("Você digitou",contador,"números.")
    print("A média desses números é",div)
    