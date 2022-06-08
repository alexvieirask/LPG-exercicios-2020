def pares_impares(l):
    p = []
    im = []
    for i in range(4):
        if l[i] % 2 == 0:
            p.append(l[i])
        else:
            l[i] % 2 == 0
            im.append(l[i])

    ls = (list(p),list(im))
    print(ls)

l = [int(input("Digite um número inteiro:")), int(input("Digite outro número inteiro:")), int(input("Digite outro número inteiro:")), int(input("Digite outro número inteiro:"))]

pares_impares(l)