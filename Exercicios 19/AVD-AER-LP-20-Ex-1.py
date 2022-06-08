N1=int(input("Digite seu primeiro número: "))
N2=int(input("Digite seu segundo número: "))
N3=int(input("Digite seu terceiro número: "))


if N1<N2 and N1<N3 : 
    print ("O número",N1,"é o menor.")
if N2<N1 and N2<N3 :
    print("O número",N2,"é o menor")
if N3<N1 and N3<N2 :
    print("O número",N3,"é o menor")

if N1==N2 and N1< N3 :
    print("O número",N1,"é o menor, pórem você digitou 2 números iguais!")

if N2==N3 and N2<N1 :
    print("O número",N2,"é o menor porém você digitou 2 números iguais!")

if N3==N1 and N3<N2:
    print("O número",N3,"é o menor porém você digitou 2 números iguais!")

if N1==N2==N3:
    print("Todos os números são iguais.")
