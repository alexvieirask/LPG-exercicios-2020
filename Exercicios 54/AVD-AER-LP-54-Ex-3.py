def imprime_n_vezes(nome, n):
    for i in range(n):
        print(nome)
        
nome=str(input("Digite uma string:"))
n=int(input("Digite quantas vezes quer que essa string seja mostrada: "))

imprime_n_vezes(nome, n)