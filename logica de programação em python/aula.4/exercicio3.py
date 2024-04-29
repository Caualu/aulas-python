nome = input("entre com seu nome:")
disciplina = input("entre com sua disciplina:")
nota1= float(input("diga a nota do primeiro bimetre:"))
nota2= float(input(" diga anota do segundo bimestre:"))
nota3= float(input(" diga a nota do terceiro bimestre:"))
nota4= float(input("diga a nota do quarto bimestre:"))

media = (nota1 + nota2 + nota3 + nota4 ) / 4


if media >= 6.0:
   print ("aprovado")

else:
   print ("reprovado")   


