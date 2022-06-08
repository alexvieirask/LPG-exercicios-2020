def ordenar_lista(l):
    
    x=True

    while x: 
        x=False

        for i in range(len(l)-1): 
            if l[i] > l[i+1]: 
                trocar(l,i) 
                x=True 

    return(l)

def trocar(l, posicao):
    
    l[posicao], l[posicao + 1] = l[posicao + 1], l[posicao]

l=[]

while True:
    n = input("Digite os números (Digite PARAR para quebrar o loop): ")
    if n=="PARAR":
        break
    else:
        l.append(int(n))

resultado=ordenar_lista(l)

print(resultado)