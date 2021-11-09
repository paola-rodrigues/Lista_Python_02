#Questão 22
'''
 Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se ˜
aposentar. As condic¸oes para aposentadoria s ˜ ao
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
'''

idade = int(input(" Digite a sua idade: "))
tempo = float(input(" Digite o tempo de serviço: "))

if idade >= 65:
        x = ("Pode se aposentar por idade")
elif tempo >= 30:
        x = ("Pode se aposentar por tempo de serviço")      
elif (idade >= 60) and (tempo >= 25):
        x = ("Pode se aposentar")
else:    
        x = "Não pode se aposentar"
    
print(x)
