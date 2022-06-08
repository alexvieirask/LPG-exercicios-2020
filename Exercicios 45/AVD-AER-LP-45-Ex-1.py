N1=int(input("Digite o primeiro número: "))
N2=int(input("Digite o segundo número: "))
CONTN1=1
CONTN2=1

FN1=N1
zero= N1>0 and N2>0



if N1 ==0 or N2==0:
    print("A multiplicação destes dois números é 0")
if zero == True:
    while CONTN1!=N1 and CONTN2!=N2:
        CONTN1=CONTN1+1
        CONTN2=CONTN2+1
        N1=FN1+N1


if N1<0 or N2<0:
    print("Você não digitou um número positivo.")
    
if zero== True:
    print("A multiplicação destes dois números é",N1)

