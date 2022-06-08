def media_turma(lista):
    um=lista[0]
    dois=lista[1]
    tres=lista[2]
    quatro=lista[3]

    media= (um+dois+tres+quatro)/4
    print("Sua média é:",media)

lista=[int(input("Digite a primeiro nota: ")),int(input("Digite a segunda nota: ")),int(input("Digite a terceira nota: ")),int(input("Digite a quarta nota: "))]

print(lista)

media_turma(lista)