def vogais_consoantes(texto):
    v = ["a","e","i","o","u","A","E","O","I","U",]
    tv = ""
    tc = ""
    espaco = 0
    for i in range(len(texto)):
        if texto[i] in v:
            tv += texto[i]
        elif texto[i] == " ":
            espaco += 1
        else:
            tc += texto[i]

    lista = [tv,tc]

    print(lista)

texto = str(input("Digite uma frase ou palavra:"))

vogais_consoantes(texto)