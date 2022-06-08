def salarios():
    lista = []
    while True:
        x=int(input("Digite o valor de vendas (-1 para quebrar o loop):"))
        if x==-1:
            break
        else:
            lista.append(x)

    v1=0
    v2=0
    v3=0
    v4=0
    v5=0
    v6=0
    v7=0
    v8=0
    v9=0

    lista_valores=[v1, v2, v3, v4, v5, v6, v7, v8, v9]
    
    for i in range(len(lista)):
        s = (lista[i] * 9) / 100 + 200
        n = int(s/100)-1
        if n > 9:
            n = 9
        elif n < 1:
            n = 1
        lista_valores[n - 1] += 1
        

    print("A quantidade de trabalhadores em cada marcador foi respectivamente:")
    print("Entre 200 e 299:", lista_valores[0])
    print("Entre 300 e 399:", lista_valores[1])
    print("Entre 400 e 499:", lista_valores[2])
    print("Entre 500 e 599:", lista_valores[3])
    print("Entre 600 e 699:", lista_valores[4])
    print("Entre 700 e 799:", lista_valores[5])
    print("Entre 800 e 899:", lista_valores[6])
    print("Entre 900 e 999:", lista_valores[7])
    print("Acima de 1000:", lista_valores[8])

salarios()