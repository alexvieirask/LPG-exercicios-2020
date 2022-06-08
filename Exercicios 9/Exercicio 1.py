#Entrada
Total_eleitores=int(input("Digite o número total de eletores: "))
brancos=int(input("Digite o número total de votos brancos: "))
nulos=int(input("Digite o número total de votos nulos: "))
validos=int(input("Digite o número total de votos validos: "))

#Processamento
Percentual_votos_brancos=(brancos/Total_eleitores)*100
Percentual_votos_nulos=(nulos/Total_eleitores)*100
Percentual_votos_validos=(validos/Total_eleitores)*100

#Saída
print("Obtiveram",Percentual_votos_brancos,"% de votos brancos.")
print("Obtiveram",Percentual_votos_nulos,"% de votos nulos.")
print("Obtiveram",Percentual_votos_validos,"% de votos validos.")
