def verifica(x):
    if x>0 and  x<5:
        Conceito="D"
    if x>=5 and x<7:
        Conceito="C"
    if x>=7 and x<9:
        Conceito="B"
    if x>=9:
        Conceito="A"

    print("Sua média:",x,"| Conceito:",Conceito)

x=float(input("Digite sua média: "))

verifica(x)