N1=int(input("Digite um número: "))
fat=0
fat1=N1

zero= N1==0
neg= N1<0

if zero == True:
    print("O fatorial do número digitado é 1")
if N1<0:
    print("Você digitou um número negativo")    

if zero== False and neg == False:
    while fat1!=1:
        fat1=fat1-1
        fat=N1*fat1
        N1=fat
        
if zero== False and neg == False:
    print("O fatorial do número digitado é",N1)

    
