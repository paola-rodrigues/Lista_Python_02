#Questão 11
n = int(input("Digite um número inteiro: "))

if n > 0:
       y =(sum(int(i) for i in str(n)))
       x = (f"O número {n} corresponde soma dos seus algarismo total {y}")         
else:
       x = "Número inválido"       
            
print(x)             

