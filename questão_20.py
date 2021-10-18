#Questão 20
'''
 Dados três valores,  A, B, C, verificar se eles podem ser valores dos
 lados de um triângulo e, se forem, se é um triângulo escaleno,
 equilátero ou isóscele, considerando os seguintes conceitos:
 
• O comprimento de cada lado de um triângulo e menor do que a soma dos outros ´
dois lados.
• Chama-se equilátero o triângulo que tem trâs lados iguais. ˆ
• Denominam-se isosceles o triângulo que tem o comprimento de dois lados iguais. ˆ
• Recebe o nome de escaleno o triângulo que tem os trâs lados diferentes.
'''

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))
       
                
if abs(b - c) < a < (b + c) or abs(a - c) < b < (a + c) or abs(a - b) < c < (a + b):
      x = "Não Forma Triângulo"      
elif (a != b and b != c and a!= c):
      x = "Triângulo Escaleno"
if(a == b and b == c):
      x = "Triângulo Equilatero"       
if(a == b and a != c) or (b == c and a != a) or (c == a and c != b):
      x = "Triângulo Isosceles"

print(x)      
