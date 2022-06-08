nome = str(input("Digite o seu nome: ")).upper()
c=len(nome)

for i in range(0, len(nome)):
    print(nome[0:c])
    c=c-1
  