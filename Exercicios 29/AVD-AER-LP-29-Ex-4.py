SP= 0
N= 0

for x in range(20):
    num=int(input("Digite seu valor númerico: "))
    
    if num>=0:
        SP=SP+num
    else:
        N= N+1

print("Soma dos números positivos:", SP)
print("Total de números negativos:",N)