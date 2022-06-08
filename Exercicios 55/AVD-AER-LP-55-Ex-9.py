def bhaskara(a,b,c):
    delta=b**2-4*a*c
    raizD=delta**0.5
    
    x1=(-b+raizD)/(2*a)
    x2=(-b-raizD)/(2*a)

    if delta<0:
        print("A equação não possui raizes reais!")
    else:
        print("x1=",x1)
        print("x2=",x2)
a=float(input("Digite o valor de A: "))
b=float(input("Digite o valor de B: "))
c=float(input("Digite o valor de C: "))

bhaskara(a,b,c)