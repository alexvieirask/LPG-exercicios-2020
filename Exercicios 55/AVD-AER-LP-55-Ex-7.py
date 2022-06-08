def media(x,n1,n2,n3):
    if x =="A":
        NF= (n1+n2+n3)/3
        print(NF)
    if x =="P":
        NF= ((n1*5)+(n2*3)+(n3*2))/10
        print(NF)
    if x =="H":
        NF= 3/((1/n1)+(1/n2)+(1/n3))
        print(NF)
        
n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))


x=str(input("Digite uma letra[A,P,H]: "))


media(x,n1,n2,n3)