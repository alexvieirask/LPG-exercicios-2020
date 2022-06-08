def potencia(x, y):  
    resultado=1
    for i in range(y):
        resultado=resultado*x
    print(resultado)
    
x=int(input("Digite o valor de x: "))
y=int(input("Digite o valor de y: "))

potencia(x,y)