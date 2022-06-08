#Entrada
salario=float(input("Escreva o seu Salário atual: R$ "))
reajuste=float(input("Escreva a porcentagem do reajuste: "))

#Processamento
porcentagem= (salario*reajuste)/100
Total=(porcentagem+salario)

#Saída
print("O seu salário com o reajuste de",reajuste,"% fica",Total,"R$ no total.")
