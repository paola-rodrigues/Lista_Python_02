# Questão 7

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
        numero = "O maior número é " + str(primeiro_numero)
elif segundo_numero > primeiro_numero:        
        numero = "O maior número é " +  str(segundo_numero)
elif primeiro_numero == segundo_numero:
        numero = "Números iguais"
        
        
print(f"{numero}")
