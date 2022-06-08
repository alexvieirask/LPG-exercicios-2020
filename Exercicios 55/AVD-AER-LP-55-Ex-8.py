def primo(x):
    mult=0

    for i in range(2,x):
        if (x % i == 0):
            mult += 1

    N=mult==0
    print(N)
x=int(input("Digite um numero: "))

primo(x)

