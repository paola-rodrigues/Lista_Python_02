#Questão 15
'''
Escreva um programa que leia um inteiro entre 1 e 7 e imprima
o dia da semana correspondente a este numero. Isto é,
domingo se 1, segunda-feira se 2, e assim por diante
'''

semana = int(input("Digite a numero inteiro entre 1 e 7: "))

if semana == 1:
       x = "domingo"         
elif semana == 2:
       x = "segunda-feira"
elif semana == 3:
       x = "terça-feira"
elif semana == 4:
       x = "quarta-feira"           
elif semana == 5:
       x = "quinta-feira"    
elif semana == 6:
       x = "sexta-feira"
elif semana == 7:
       x = "sábado"
else:
       x = "Número inválido" 
            
print(x)                                                                                                                                     
