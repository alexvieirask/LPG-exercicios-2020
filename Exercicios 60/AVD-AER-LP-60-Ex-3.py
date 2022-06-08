def inverte_duplo(t):
    um=t[0]
    dois=t[1]
    tres=t[2]
    quatro=t[3]

    um=um[::-1]
    dois=dois[::-1]
    tres=tres[::-1]
    quatro=quatro[::-1]

    t=[quatro,tres,dois,um]
    print(t)

t=[str(input("Digite o primeiro item da lista: ")),str(input("Digite o segundo item da lista: ")),str(input("Digite o terceiro item da lista: ")),str(input("Digite o quarto item da lista: "))]

inverte_duplo(t)