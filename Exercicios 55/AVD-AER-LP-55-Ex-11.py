def perfeito(x):
    soma=0
    for i in range(1,x):
        if x % i == 0:
            soma = soma+i
    n= x == soma
    print (n)

x=int(input("Digite um número: "))
perfeito(x)