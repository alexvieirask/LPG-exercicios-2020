def conta_digitos(a,b):    
    a=str(a)
    b=str(b)
    if len(a) != len(b):
        print("Os números inseridos possuem um número de casas diferentes")
    else:
        a1=a.count("1")
        a2=a.count("2")
        a3=a.count("3")
        a4=a.count("4")
        a5=a.count("5")
        a6=a.count("6")
        a7=a.count("7")
        a8=a.count("8")
        a9=a.count("9")

        b1=b.count("1")
        b2=b.count("2")
        b3=b.count("3")
        b4=b.count("4")
        b5=b.count("5")
        b6=b.count("6")
        b7=b.count("7")
        b8=b.count("8")
        b9=b.count("9")
        if a1 == b1 and a2 == b2 and a3 == b3 and a4 == b4 and a5 == b5 and a6 == b6 and a7 == b7 and a8 == b8 and a9 == b9:
            print("O número",a,"é sim, uma permutação do número",b,".")
        else:
            print("O número",a,"não é uma permutação do número",b,".")

a=int(input("Digite um número inteiro positivo sem a presença de dígitos de 0:"))

b=int(input("Digite outro número, permutação do número anterior:"))

conta_digitos(a,b)