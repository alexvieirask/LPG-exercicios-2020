N=int(input("Digite um número inteiro positivo: "))
i=1
A=0
arm=0

#Coloquei nomes aleatórios para as variáveis

if N<=0:
    print("Você não digitou um número inteiro positivo!")
else:
    while i<N:
        i=i+1
        A=A+1/i
        arm=A
        A=arm


if N==1:
    print(2)

if N>1:
    print(A+1)