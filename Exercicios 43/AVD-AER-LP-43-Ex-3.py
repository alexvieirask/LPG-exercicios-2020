i=int(input("Digite um numero inteiro positivo:"))
calc=0
contador=0

if i ==0:
   i=calc+1

while i != 0:
    contador=contador+1
    calc=i//10
    i=calc

print("Seu número tem", contador,"dígitos.")