lista=[]
while True:
    n=int(input("Digite uma das notas (-1 para quebrar o loop): "))
    if n==-1:
        break
    else:
        lista.append(n)

def questao2(lista):
    print("Foram apresentados", len(lista),"valores.")
    print("Foram eles:", lista)
    print("Ao contrário ficam:",lista[::-1])
    print("A soma deles é:", sum(lista))
    m = sum(lista)/len(lista)
    print("A média é:",m)
    x = []
    for i in range(len(lista)):
        if lista[i]>m:
            x.append(lista[i])
    print("Os acima da média são:",x)
    y=[]
    for i in range(len(lista)):
        if lista[i]<7:
            y.append(lista[i])
    print("Os abaixo de 7 são:",y)

        
questao2(lista)
