#Questão 18
'''
Faça um programa que mostre ao usuario um menu com 4 opcões de operaçõess ma˜temáticas
(as básicas, por exemplo).O usuário escolhe uma das opcões e o seu programa então pede
dois valores numéricos e realiza a operacão, mostrando o resultado e saindo ˜
'''
operacao = input("Digite a operação desejada (adição), (subtração), (divisão), (multiplicação): ")
nume1 = float(input("Digite o primeiro número: "))
nume2 = float(input("Digite o segundo número: "))

if operacao == "adição":
        x = (f" O resultado de sua {operacao} é {nume1 + nume2}")
        
elif operacao == "subtração":
        x = (f" O resultado de sua {operacao} é {nume1 - nume2}")
        
elif operacao == "divisão":
        x = (f" O resultado de sua {operacao} é {nume1 / nume2}")
        
elif operacao == "multiplicação":
        x = (f" O resultado de sua {operacao} é {nume1 * nume2}")          
        
else:
        x = "Operação inválida" 
            
print(x)
print("saindo")
