def salarios():
    lista=[]
    while True:
        x=int(input("Digite o valor de vendas (-1 para quebrar o loop): "))
        if x==-1:
            break
        else:
            lista.append(x)

    v1=0
    v2=0
    v3=0
    v4=0
    v5=0
    v6=0
    v7=0
    v8=0
    v9=0

    for i in range(len(lista)):
        salario = (lista[i] * 9) / 100 + 200
        if salario >= 200 and salario<= 299:
            v1+=1
        elif salario>=300 and salario<= 399:
            v2+=1
        elif salario>=400 and salario<=499:
            v3+= 1
        elif salario>=500 and salario<=599:
            v4+=1
        elif salario>=600 and salario<=699:
            v5+=1
        elif salario>=700 and salario<=799:
            v6+=1
        elif salario>=800 and salario<=899:
            v7+=1
        elif salario>=900 and salario<=999:
            v8+=1
        elif salario > 999:
            v9 += 1


    print("Entre 200 e 299:",v1)
    print("Entre 300 e 399:",v2)
    print("Entre 400 e 499:",v3)
    print("Entre 500 e 599:",v4)
    print("Entre 600 e 699:",v5)
    print("Entre 700 e 799:",v6)
    print("Entre 800 e 899:",v7)
    print("Entre 900 e 999:",v8)
    print("Acima de 1000:",v9)

salarios()