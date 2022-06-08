N1=int(input("Digite o primeiro número: "))
N2=int(input("Digite o segundo número: "))

if N1>N2: 
    maior=N1
    menor=N2
else:
    menor=N1
    maior=N2

if maior%menor==0 :
    print("Os números",menor,"e",maior,"são múltiplos.")
else:
    print("Os números",menor,"e",maior,"não são múltiplos.")