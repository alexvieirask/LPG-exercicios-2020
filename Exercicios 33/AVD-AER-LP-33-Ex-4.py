anterior=0
proximo=1
soma=1

N=20

for i in range(0,N):
    print(anterior)
    soma=proximo+anterior
    anterior=proximo
    proximo=soma

