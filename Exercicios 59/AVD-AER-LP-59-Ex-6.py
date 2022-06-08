def verifica(x,y,z):
    if x>=1 and x<32:    #Considerei 31 dias por mês.
        x=True
    else:
        x=False
        a=-1
    
    if y>0 and y<=12:
        y=True
    else:
        y=False
        b=-2
    if z<10000 and z>0:
        z=True
    else:
        z=False
        c=-4
    if x==False:
        a=-1
    else:
        a=0
    if y==False:
        b=-2
    else:
        b=0

    if z==False:
        c=-4
    else:
        c=0

    print(a+b+c)

x=int(input("Digite o dia(DD):"))
y=int(input("Digite o mês(MM):"))
z=int(input("Digite o ano(AAAA):"))

verifica(x,y,z)