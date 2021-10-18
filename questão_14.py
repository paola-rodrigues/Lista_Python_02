#Questão 14
'''
 A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo
de 0 ate 10, respectivamente, a um trabalho de laboratório, a uma avaliacão semestral ˜
e a um exame final. A média das três notas mencionadas anteriormente obedece aos 
pesos: Trabalho de Laboratorio: 2; Avaliacão Semestral: 3; Exame Final: 5. De acordo ˜
com o resultado, mostre na tela se o aluno esta reprovado (média entre 0 e 2,9), de 
recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificacões necessárias.
'''

PESO1 = 2 #Laboratorio
PESO2 = 3 #Avaliacão Semestral
PESO3 = 5 #Exame Final

nota1 = float(input("Digite a primeira nota de 0 até 10: "))
nota2 = float(input("Digite a segunda nota de 0 até 10:  "))
nota3 = float(input("Digite a terceira nota de 0 até 10: "))


n = (nota1 * PESO1) + (nota2 * PESO1) +(nota3 * PESO3)
soma = PESO1 + PESO1 + PESO3
media = (n/soma)

if media >= 5.0:
       x = (f"Sua média foi {media:.2f}, aluno foi aprovado")         
elif media >= 3.0:
       x = (f"Sua média foi {media:.2f}, aluno em recuperação")
else:
       x = (f"Sua média foi {media:.2f}, aluno está reprovado")    
            
print(x)                                                                                                                                     
