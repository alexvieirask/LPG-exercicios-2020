N1=str(input("Digite o primeiro número: "))
N2=str(input("Digite o segundo número: "))
y=len(N1)
x=0
n=True

if len(N1) != len(N2):
    print("Os números que você digitou são de tamanhos diferentes")
else:
    for i in range(0,y):
        c=(N1[x:x+1])
        d=(N2[x:x+1])
        x=x+1
        val=c<d
        
        if val== False:
            n=val

print(n)




