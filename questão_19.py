#Questão 19
'''
Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou
5, mas não simultaneamente pelos dois.  ˜
'''

num = int(input("Digite um número inteiro: "))

if num % 3 == 0:
        x = (f"O número {num} é  divisível por 3")
        
elif num % 5 == 0:
        x = (f" O número {num} é  divisível por 5")
    
else:
        x = "Operação inválida" 
            
print(x)

