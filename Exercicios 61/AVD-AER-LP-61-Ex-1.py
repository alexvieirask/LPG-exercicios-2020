def temperaturas_medias():
    t=[int(input("Digite a temperatura media de Janeiro: ")), 
    int(input("Digite a temperatura media de Fevereiro: ")), 
    int(input("Digite a temperatura media de Março: ")), 
    int(input("Digite a temperatura media de Abril: ")), 
    int(input("Digite a temperatura media de Maio: ")), 
    int(input("Digite a temperatura media de Junho: ")), 
    int(input("Digite a temperatura media de Julho: ")),
    int(input("Digite a temperatura media de Agosto: ")), 
    int(input("Digite a temperatura media de Setembro: ")), 
    int(input("Digite a temperatura media de Outubro: ")), 
    int(input("Digite a temperatura media de Novembro: ")),
    int(input("Digite a temperatura media de Dezembro: "))]
    s=0
    
    for i in range(len(t)):
        s+=t[i]
    m=s/12

    print("A média da temperatura total do ano:", m)

    mx = []

    if t[1]>m:
        mx.append("1-Janeiro")
    if t[2]>m:
        mx.append("2-Fevereiro")
    if t[3]>m:
        mx.append("3-Março")
    if t[4]>m:
        mx.append("4-Abril")
    if t[5]>m:
        mx.append("5-Maio")
    if t[6]>m:
        mx.append("6-Junho")
    if t[7]>m:
        mx.append("7-Julho")
    if t[8]>m:
        mx.append("8-Agosto")
    if t[9]>m:
        mx.append("9-Setembro")
    if t[10]>m:
        mx.append("10-Outubro")
    if t[11]>m:
        mx.append("11-Novembro")
    else:
        mx.append("12-Dezembro") 
   
    print("Os meses acima da média são:", mx)
    
        
temperaturas_medias()
