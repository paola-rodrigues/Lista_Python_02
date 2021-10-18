import math
#Questão 13
'''
Faça um algoritmo que calcule a media ponderada das notas de 3 provas. A primeira e
a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a mêdia do aluno 
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou ˜
superior a 60 pontos.

'''
PESO1 = 1 #Primeira e segunda prova
PESO2 = 2 #terceira prova

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:  "))
nota3 = float(input("Digite a terceira nota: "))


n = (nota1 * PESO1) + (nota2 * PESO1) +(nota3 * PESO2)
soma = PESO1 + PESO1 + PESO2
media = (n/soma)

if media * 10 >= 60:
       x = (f"Sua média foi {media}, aluno foi aprovado")         
else:
       x = (f"Sua média foi {media}, aluno foi reprovado")        
            
print(x)                                                                                                                                     
