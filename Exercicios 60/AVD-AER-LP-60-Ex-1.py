def min_max(t):
    contador=0
    maior=lista1[0]
    menor=lista1[0]

    while contador<len(lista1):
        if lista1[contador]<menor:
            menor=lista1[contador]
        if lista1[contador]>maior:
            maior=lista1[contador]
        contador+=1

    lista2=[menor, maior]

    print(lista2)

lista1=[int(input("Digite o primeiro número da lista: ")),int(input("Digite o segundo número da lista: ")),int(input("Digite o terceiro número da lista: ")),int(input("Digite o quarto número da lista: ")),int(input("Digite o quinto número da lista: "))]

min_max(lista1)