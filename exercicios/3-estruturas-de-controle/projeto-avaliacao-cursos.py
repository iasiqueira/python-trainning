# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos = ("Java","R","Python","React","Node")
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso1 = "Python"
curso2 = "Java"
curso3 = "Powercenter"
# 3. Crie um dicionário vazio para armazenar a nota do curso
notas = {}
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

if curso1 in cursos:
  print (f"O curso {curso1} está no catalogo de cursos.")
  notas[curso1] = int(input("Por favor, avalie o curso: (Notas 0 a 5)"))
else:
  print (f"Não possuimos o curso {curso1} em nosso catalogo.")
  notas[curso1] = int(input("Por favor, avalie o curso: (Notas 0 a 5)"))
if curso2 in cursos:
  print (f"O curso {curso2} está no catalogo de cursos.")
  notas[curso2] = int(input("Por favor, avalie o curso: (Notas 0 a 5)"))
else:
  print (f"Não possuimos o curso {curso2} em nosso catalogo.")

if curso3 in cursos:
  print (f"O curso {curso3} está no catalogo de cursos.")
  notas[curso3] = int(input("Por favor, avalie o curso: (Notas 0 a 5)"))
else:
  print (f"Não possuimos o curso {curso3} em nosso catalogo.")

print ("*" * 50)
print (f"Muito obrigado! \n Seguem as avaliações dos nossos cursos: \n {notas}")