def eh_bissexto(ano):
    
    x= ano %100!=0 and ano %4 ==0 or ano %400 ==0
    print(x)
    
ano=int(input("Digite o Ano para ser verificado: "))

eh_bissexto(ano)