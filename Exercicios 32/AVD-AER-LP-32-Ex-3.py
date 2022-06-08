N= int(input("Digite o valor de N: "))

A=0

for x in range(1,N,2):
    A=A+(1/x)
    print(A)