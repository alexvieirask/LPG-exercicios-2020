x=str(input("Digite uma palavra: "))
y=len(x)-1
z=len(x)

for i in range(0,len(x)):
    print(x[y:z])
    y=y-1