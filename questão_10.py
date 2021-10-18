# Questão 10

altura = float(input("Digite sua altura:   "))
sexo = input("Digite o seu sexo Homem e Mulher: ")

if sexo == "Homem" or sexo == "homem":
        formula = (72.7 * altura) - 58
elif sexo == "Mulher" or sexo == "mulher":
        formula = (62.1 * altura) - 44.7      
        
print(f"O seu peso ideal para um {sexo} é {formula:.2f}")
