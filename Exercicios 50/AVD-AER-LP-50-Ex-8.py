x=str(input("Digite uma frase: "))
s= x.count(" ")

A= x.count("A")
a= x.count("a")
asoma= A+a


E= x.count("E")
e= x.count("e")
esoma= E+e


I= x.count("I")
i= x.count("i")
isoma= I+i


O= x.count("O")
o= x.count("o")
osoma= O+o


U= x.count("U")
u= x.count("u")
usoma= U+u


print("Vogais em sua frase")
print("-"*30)
print("A:",asoma)
print("E:",esoma)
print("I:",isoma)
print("O:",osoma)
print("U:",usoma)
print("Sua frase possui", s,"espaços em branco.")