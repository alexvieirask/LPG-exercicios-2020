def idade(x):
    if x>=5 and x<=7:
        print("INFANTIL A")
    if x>=8 and x<=10:
        print("INFANTIL B")
    if x>=11 and x<=13:
        print("JUVENIL A")
    if x>=14 and x<=17:
        print("JUVENIL B")
    if x>=18:
        print("ADULTO")
x=int(input("Digite sua idade: "))
idade(x)