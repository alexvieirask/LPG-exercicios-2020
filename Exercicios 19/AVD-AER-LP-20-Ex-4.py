print("Digite os Valores do triângulo para ser verificado.")
X=float(input("Escreva o valor de um dos lados do triângulo: "))
Y=float(input("Escreva o valor do segundo lado do triângulo: "))
Z=float(input("Escreva o valor do ultimo lado do triângulo: "))

if X<Y+Z and Y<X+Z and Z<X+Y:
    print("As medidas acima podem formar um triângulo: ")
    if X==Y==Z:
        print("Triângulo Equilátero.")
    elif X!=Y!=Z!=X:
        print("Triângulo Escaleno.")
    else:
        print("Triângulo Isósceles.")
        
else:
    print("As medidas acima não podem formar um triângulo.")
      