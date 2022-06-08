data=int(input("Digite a data para ser invertida no formato DDMMAA: "))

DD= data//10000
AA= data%100

novoDD= DD//1
novoAA=AA*10000

time= data%10000
MM= time// 100
novoMM=MM*100


print("A data invertida fica:",DD,MM,AA)