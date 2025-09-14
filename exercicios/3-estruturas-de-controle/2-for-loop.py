# Crie uma lista
print ("*" * 50)
lista_exemplo = ("Italo", "37 anos", 1.74, 13000)
print (lista_exemplo)
# Crie um for loop para imprimir cada elemento dessa lista
print ("*" * 50)
for item in lista_exemplo:
  print (f"Item: {lista_exemplo.index(item)} - Valor: {item}")
# Crie um objeto iterável utilizando a função range()
print ("*" * 50)
lista_exemplo2 = list(range(1,11))
print (lista_exemplo2)
# Use esse objeto iterável para criar um for loop que imprima na tela a frase "Estou aprendendo uma linguagem de programação."
for item in lista_exemplo2:
  print (f"Item: {lista_exemplo2.index(item)} - Valor: {item} -  Frase: Estou aprendendo uma linguagem de programação.")
