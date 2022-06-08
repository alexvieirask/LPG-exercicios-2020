def verifica(x):
    N=x>0
    print("O número que você digitou é positivo?",N)


x=int(input("Digite um número: "))

if x==0:
    print("Você digitou o número 0, ou seja, é neutro.")
else:
    verifica(x)
