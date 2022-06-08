maior=0
menor=0
primeiro=True


while True:
    i=(input("Digite um  número(Use fim para terminar): "))
    if i == "fim":
        break
    else:
        i=float(i)
        if primeiro:
            maior=i
            menor=i
            primeiro=False
        
        if i < menor:
            menor=i
        elif i>maior:
            maior=i

if primeiro:
    print("Você não digitou um número!")
else:
    print("O menor número foi:",menor)
    print("O menor número foi:",maior)
