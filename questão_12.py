import math
#Questão 12
'''
Ler um numero inteiro. Se o n ´ umero lido for negativo, escreva a mensagem “N ´ umero ´
invalido”. Se o n ´ umero for positivo, calcular o logaritmo deste numero
'''

n = int(input("Digite um número: "))

if n > 0:
       logaritimo = math.log(n)
       x = (f"O logaritimo é: {logaritimo:.2f}")         
else:
       x = "Número inválido"       
            
print(x)                                                                                                                                         
