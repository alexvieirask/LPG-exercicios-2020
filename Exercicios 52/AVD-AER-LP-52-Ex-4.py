s1=str(input("Digite a primeira palavra: "))
s2=str(input("Digite a segunda palavra: "))
x=0
h=len(s1) >= len(s2)


s4=""
s3=""
s5=""

if h == True:
    for i in range(0,len(s1)):
        s4=s5
        c=(s1[x:x+1])
        d=(s2[x:x+1])
        x=x+1
        s3=c+d
        s5=s4+s3
else:
    for i in range(0,len(s2)):
        s4=s5
        c=(s1[x:x+1])
        d=(s2[x:x+1])
        x=x+1
        s3=c+d
        s5=s4+s3


print(s5)
