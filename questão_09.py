# Questão 9

salario = float(input("Digite seu salário R$  "))
emprestimo = float(input("Digite o valor do empréstimo R$ "))

x = salario * 0.2

if emprestimo <= x:
        numero = " Empréstimo concedido"
else:
        numero = "Empréstimo não concedido"
        
        
print(f"{numero}")
