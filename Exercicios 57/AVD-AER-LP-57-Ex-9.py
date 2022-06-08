def encaixa(a,b):
    a=str(a)
    b=str(b)
    c=len(a)
    e=len(b)
    
    d=a[c-e:c+e]
  
    if b == d:
        print("Encaixa")
    else:
        print("Não encaixa")



a=int(input("Digite o valor de A: "))
b=int(input("Digite o valor de B: "))

encaixa(a,b)