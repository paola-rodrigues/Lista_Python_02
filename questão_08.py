# Questão 8

primeira = float(input("Digite o primeira nota: "))
segunda = float(input("Digite o segunda nota: "))
x =(primeira >= 0.0) and (primeira  <= 10.0)
y =(segunda  >= 0.0) and (segunda   <= 10.0)

if x and y:
        numero = "Sua média foi " + str((primeira + segunda)/2)
else:
        numero = "Nota invalida, a nota tem que está entre o valor 0.0 e 10.0"
        
        
print(f"{numero}")
