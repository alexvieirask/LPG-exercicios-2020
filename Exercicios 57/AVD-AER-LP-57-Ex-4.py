def digito(n):
    if n > 0:
        n=str(n)
        x=n[:1]

        print("O primeiro dígito do número inserido é", x)
    else:
        print("O número inserido não é positivo")

n=int(input("Digite um número: "))

digito(n)