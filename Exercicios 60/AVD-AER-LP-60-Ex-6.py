lista = []

while True:
    l = float(input("Digite as notas dos alunos(-1 para parar):"))
    if l == -1:
        break
    elif l < 0 or l > 10:
        print("O número inserido não é uma nota válida")
    else:
        lista.append(l)

def media_turma(lista):
    t = 0.0

    for i in range(len(lista)):
        t += lista[i]

    m = t / (i + 1)

    c = 0
    maior = lista[0]
    menor = lista[0]

    while c < len(lista):
        if lista[c] < menor:
            menor = lista[c]
        if lista[c] > maior:
            maior = lista[c]
        c += 1

    f = [m,maior,menor]

    print(f)

media_turma(lista)
