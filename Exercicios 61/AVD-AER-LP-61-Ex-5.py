def gera_lista(n):
    
    x = []
    
    for i in range(n):
        x.append(i)
    x.append(n)

    print(x)

gera_lista(int(input("Digite o número desejado:")))