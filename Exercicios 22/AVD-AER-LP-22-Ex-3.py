data=int(input("Escreva a data para ser verificada(DDMMAAAA): "))

DD=data//1000000
AA=data%100

MM=data//10000
novoMM= MM%100

if DD*novoMM==AA:
    print("Parabéns!")
    print("Essa data é Mágica!")
else:
    print("Essa data não é considerada uma data mágica!")
