N=int(input("Digite o valor de N: "))

A=0

for i in range(1,N+1):
    if i%2 ==0:
        A=A-(1/i)
    else:
        A=A+(1/i)
    print(A)


    #Obs: Nao consegui realizar a quinta questão.