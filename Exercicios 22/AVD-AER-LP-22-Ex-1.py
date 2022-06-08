Ano=int(input("Digite o Ano para ser verificado: "))
if Ano %100!=0 and Ano %4 ==0 or Ano %400 ==0:
    print("Esse ano é Bissexto!")
else:
    print("Esse ano não é Bissexto!")