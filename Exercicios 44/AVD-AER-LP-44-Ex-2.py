N=int(input("Digite um número inteiro positivo: "))
i=1
A=0
calc=0
baixo=1
bau=0
ult=1

#Coloquei nomes aleatórios para as variáveis


if N<=0:
    print("Você não digitou um número inteiro positivo!")
else:
    while i<=N:
        i=i+1
        calc=calc+1
        baixo=baixo+1
        bau=bau+(N-calc)/baixo
        A=A+bau
    
    if A==N:
        ult=ult/N
        A=A+ult

            
if N>=1:
    print(A+N)