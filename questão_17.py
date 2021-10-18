#Questão 17
'''
Faça um programa que calcule e mostre a area de um trapézio
'''

base_maior = float(input("Digite a base maior do trapézio: "))
base_menor = float(input("Digite a base menor do trapézio: "))
altura = float(input("Digite a altura do trapézio: "))

if int(base_maior) > 0 and int(base_menor) > 0 :
       area = ((base_maior + base_menor )* altura ) / 2        
       x = (f" A área do trapézio é {area}")  
else:
       x = "Número inválido" 
            
print(x)                                                                                                                                     
