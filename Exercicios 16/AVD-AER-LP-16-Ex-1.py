num=int(input("Informe um número para ser verificado: "))

E=  num // 1%10
D=  num // 10%10
C=  num // 100%10
B=  num // 1000%10
A=  num // 10000%10

S=(6*A)+(5*B)+(4*C)+(3*D)+(2*E)

DigitoV= S%7

print("Seu dígito verificador é",DigitoV)