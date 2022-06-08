def peso(alt,sexo):
    if sexo == "feminino":
        ideal=int(62.1*alt-44.7)
        print("Seu peso ideial é:",ideal,"KG")
    if sexo== "masculino":
        ideal=int(72.7*alt-58)
        print("Seu peso ideial é:",ideal,"KG")

sexo=str(input("Você é do sexo masculino ou feminino: "))

alt=float(input("Digite sua altura: "))

peso(alt,sexo)