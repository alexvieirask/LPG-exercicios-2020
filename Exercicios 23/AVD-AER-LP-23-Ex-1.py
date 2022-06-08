a=float(input("Digite o valor de A: "))
b=float(input("Digite o valor de B: "))
c=float(input("Digite o valor de C: "))

delta=b**2-4*a*c
raizD=delta**0.5

x1=(-b+raizD)/2*a

x2=(-b-raizD)/2*a

if delta<0:
    print("A equação não possui raizes reais!")

if delta ==0:
    print("A equação possui uma raíz real!")
    print("x1=",x1)


if delta>0:
    print("A equação possui duas raízes reais!")
    print("x1=",x1)
    print("x2=",x2)
   
