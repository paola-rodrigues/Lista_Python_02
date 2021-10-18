#Questão 16
'''
Escreva um programa que leia um inteiro entre 1 e 12
e imprima o mês correspondente a este numero. Isto é,
janeiro se 1, fevereiro se 2, e assim por diante.
'''

mes = int(input("Digite a numero inteiro entre 1 e 12: "))

if mes == 1:
       x = "janeiro"         
elif mes == 2:
       x = "fevereiro"
elif mes == 3:
       x = "março"
elif mes == 4:
       x = "abril"           
elif mes == 5:
       x = "maio"    
elif mes == 6:
       x = "junho"
elif mes == 7:
       x = "julho"
elif mes == 8:
       x = "agosto"
elif mes == 9:
       x = "setembro"
elif mes == 10:
       x = "outubro"
elif mes == 11:
       x = "novembro"
elif mes == 12:
       x = "dezembro"       
else:
       x = "Número inválido" 
            
print(x)                                                                                                                                     
