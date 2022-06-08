def digitos(n):
    calc=0
    contador=0

    if n ==0:
        n=calc+1

    while n != 0:
        contador=contador+1
        calc=n//10
        n=calc
    
    print("Seu número tem", contador,"dígitos.")

n=int(input("Digite um número:"))

digitos(n)