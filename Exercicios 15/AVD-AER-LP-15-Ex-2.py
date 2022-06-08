matricula=int(input("Digite a sua matricula no formato AASDDDD: "))
ano= matricula//10000

Tempo=matricula%10000
Semestre=Tempo//1000    

print("A matricula foi realizada no ano",ano,"e feita no semestre",Semestre)