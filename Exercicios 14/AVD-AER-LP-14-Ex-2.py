num=int(input("informe seu número com três digitos:"))


centena=int(num//100%10)
dezena=int(num//10%10)
unidade=int(num//1%10)

print("Centena=",centena)
print("Dezena=",dezena)
print("Unidade=",unidade)