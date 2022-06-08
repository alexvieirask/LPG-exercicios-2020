#Entrada
suco=float(input("Digite o valor do suco em Reais: " ))
sobremesa=float(input("Digite o valor da sobremesa em Reais: "))
prato_principal=float(input("Digite o valor do prato pricipal em Reais: "))

#Processamento
Soma=(suco+sobremesa+prato_principal)
acrescimo=(Soma)*10/100
Total=(Soma+acrescimo)

#Saida
print("O valor total da refeição:",Total,"Reais.")