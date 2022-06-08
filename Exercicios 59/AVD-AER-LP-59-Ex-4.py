def verificador(x):
    if x==0 or x<0:
        print("O número que você digitou é neutro ou negativo.")
    else:
        x=x%2
        x=x<1
        print (x)


x=int(input("Digite um número: "))

verificador(x)