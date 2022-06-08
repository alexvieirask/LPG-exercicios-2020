def dias(x,y,z):
    y=y*30
    x=x*365
    print("Total de Dias:",y+x+z,)
x=int(input("Digite a quantidade de anos: "))
y=int(input("Digite os meses(30 dias): "))
z=int(input("Digite os dias: "))
dias(x,y,z)