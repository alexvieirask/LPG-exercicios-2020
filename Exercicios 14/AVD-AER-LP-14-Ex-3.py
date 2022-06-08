num=int(input("Digite o número de três digitos para fazer a inversão:"))

C=int(num//100%10)
D=int(num//10%10)
U=int(num//1%10)

C2=int(C)
D2=int(D*10)
U2=int(U*100)

M=(U2+D2+C2)
print("Seu número invertido é:",M)