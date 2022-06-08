soma=0
maior=0
menor=n


for x in range(1,11):
    n=int(input("Digite seu valor: "))
    soma=soma+n
    media=float(soma/10) 
    
    
    if n> maior:
        maior=n
    
    if n< menor:
        menor=n
    
print("Menor: ",menor,"    ""Maior: ",maior,"    ""Média: ",media)
    