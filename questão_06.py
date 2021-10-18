# Questão 6

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
        x = primeiro_numero - segundo_numero
        numero = primeiro_numero
elif segundo_numero > primeiro_numero:
        x = segundo_numero - primeiro_numero
        numero = segundo_numero
        
print(f"O número maior é {numero} a diferença entre os dois números é {x}")
