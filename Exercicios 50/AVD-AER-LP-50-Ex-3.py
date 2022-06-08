nome = str(input("Digite o seu nome: ")).upper()
c=len(nome)

for i in range(0, len(nome)+1):
    print(nome[:i])