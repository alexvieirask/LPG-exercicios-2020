palavra=str(input("Digite uma palavra: "))
inversa=str(input("Digite essa palavra na ordem inversa: "))

inv= (palavra[::-1])

if inversa == inv:
    print(inversa,"é o inverso de",palavra,"!")
else:
    print(inversa,"não é o inverso de",palavra,"!")