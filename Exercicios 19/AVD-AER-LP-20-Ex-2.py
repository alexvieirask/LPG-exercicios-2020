N1=int(input("Digite seu primeiro número: "))
N2=int(input("Digite seu segundo número: "))
N3=int(input("Digite seu terceiro número: "))

if N1>N2>N3 :
    print(N1,N2,N3)

if N1>N3>N2 :
    print(N1,N3,N2)

if N2>N1>N3 :
    print(N2,N1,N3)

if  N2>N3>N1 :
    print(N2,N3,N1)

if N3>N1>N2 :
    print(N3,N1,N2)

if N3>N2>N1 :
    print(N3,N2,N1)

if N1== N2 and N1>N3:
    print(N1,N2,N3)

if N1== N2 and N1<N3:
    print(N3,N2,N1)

if N2== N3 and N2>N1:
    print (N2,N3,N1)

if N2== N3 and N2<N1:
    print (N1,N3,N2)

if N3==N1 and N3>N2 :
    print(N3,N1,N2)

if N3==N1 and N3<N2 :
    print(N2,N1,N3)

if N1==N2==N3:
    print(N1,N2,N3)