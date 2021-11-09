#Questão 21
'''
21. Escreva o menu de opc¸oes abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida. ´
Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).
'''
a = print("Escolha a opção: \n 1- Soma de 2 números.\n \
2- Diferença entre 2 números (maior pelo menor).\n \
3- Produto entre 2 números.\n \
4- Divisão entre 2 números (o denominador não pode ser zero).\n")


opcao = int(input(" Digite a opção escolhida: "))
numero_1 = float(input(" Digite o primeiro número: "))
numero_2 = float(input(" Digite o segundo número: "))
if opcao == 1:
   x = (f" A soma do {numero_1} + {numero_2} = {numero_1 + numero_2}")
elif opcao == 2:
   if numero_1 > numero_2:
      x = (f" A diferença do {numero_1} - {numero_2} = {numero_1 - numero_2}")
   elif numero_2 > numero_1:
      x = (f" A diferença do {numero_2} - {numero_1} = {numero_2 - numero_1}")      
elif opcao == 3:
      x = (f" A multiplicação do {numero_1} * {numero_2} = {numero_1 * numero_2}")
elif opcao == 4:
   if numero_2 > 0:   
      x = (f" A soma do {numero_1} / {numero_2} = {numero_1 / numero_2}")
   else:
      x = "O segundo número tem ser maior que zero que é o denominador"
else:    
      x = "Erro: Opção Inválida"
    
print(x)
