# Declare 4 variáveis do tipo numérica
num1 = 13
num2 = 13
num3 = 13
num4 = 5

# Crie uma estrutura condicional para comparar dois números
print ("*" * 50)
if num1 > num2:
# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
  print(f'Condição foi cumprida. {num1} é maior que {num2}')
# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
else:
  print(f'Condição não foi cumprida. {num1} é menor que {num2}')

# Insira outras condições na estrutura condicional usando o elif
print ("*" * 50)
if num3 > num4:
  print(f'Condição 1 foi cumprida. {num3} é maior que {num4}')
elif num3 == num4:
  print(f'Condição 2 foi cumprida. {num3} é igual {num4}')
else:
  print(f'Nenhuma das condições foram cumpridas. {num3} é menor que {num4}')

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
print ("*" * 50)
if num3 > num4 and num1 > num2:
  print(f'Condição 1 foi cumprida. {num3} é maior que {num4} e {num1} é maior que {num2}')
elif num3 == num4 and num1 == num2 :
  print(f'Condição 2 foi cumprida. {num3} é igual {num4} e {num1} é igual a {num2}')
elif num3 < num4 or num1 < num2:
    print(f'Condição 3 foi cumprida. {num3} é menor {num4} ou {num1} é menor que {num2}')
else:
  print(f'Nenhuma das condições foram cumpridas. {num3} é menor ou igual a {num4} ou {num1} é menor ou igual a {num2}')

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
print ("*" * 50)
if num3 > num4:
  print(f'Condição 1 foi cumprida. {num3} é maior que {num4}')
if num1 == num2:
  print(f'Condição 1 foi cumprida. {num1} é igual a {num2}')