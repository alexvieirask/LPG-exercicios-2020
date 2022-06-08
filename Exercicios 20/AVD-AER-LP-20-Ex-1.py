N1=float(input("Digite a primeira nota: "))
N2=float(input("Digite a segunda nota: "))

media=(N1+N2)/2
if media >= 5:
    print("Você teve média",media,",Parabéns!")
    print("Você foi aprovado!")
else:
    print("Você teve média",media,)
    print("Você foi reprovado!")