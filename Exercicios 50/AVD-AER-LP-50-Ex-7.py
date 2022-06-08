um=str(input("Digite uma frase: "))
dois=str(input("Digite uma frase: "))

x= len(um)
y= len(dois)

print("-"*30)

print("Tamanho de", um, ":", x)
print("Tamanho de", dois, ":", y)

print("-"*30)

if x == y:
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")


if um == dois:
    print("As duas strings possuem conteúdo igual.")
else:
    print("As duas strings possuem conteúdo diferente.")
