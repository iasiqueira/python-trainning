# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
lista_exercicio = list(range(20,40))
# 2. Crie um for loop para percorrer todos os elementos da lista
for item in lista_exercicio:
# 3. Crie uma estrutura condicional para verificar cada número da lista:
  item_lista = lista_exercicio.index(item)
  if (item % 3 == 0) and  (item % 5 == 0):
    lista_exercicio[item_lista] = "FizzBuzz"
  elif (item % 3 == 0):
    lista_exercicio[item_lista] = "Fizz"
  elif (item % 5 == 0):
    lista_exercicio[item_lista] = "Buzz"
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"
print (lista_exercicio)
