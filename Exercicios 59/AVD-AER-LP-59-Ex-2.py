def quantidade(x,y):
    if len(x)>len(y):
        print("*"*len(x))
        print(x)
        print(y)
        print("*"*len(x))
    else:
        print("*"*len(y))
        print(x)
        print(y)
        print("*"*len(y))

x=str(input("Digite seu nome: "))
y=str(input("Digite a disciplina: "))

quantidade(x,y)