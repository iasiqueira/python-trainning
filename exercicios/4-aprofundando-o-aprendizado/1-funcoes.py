# Crie uma função para selecionar o curso desejado em uma trilha profissional
def selecionar_curso():
  curso = int(input(f'Informe o curso desejado: \n 1 - Introdução a SQL \n 2 - Python: Formação Básica \n'))
  return curso

# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
def percorrer_curso(curso_escolhido):
  trilha = {1: {'titulo': 'Introdução a SQL', 'total_niveis': 3}, 2: {'titulo': 'Python: Formação Básica', 'total_niveis': 7}}
  curso_corrente = trilha[curso_escolhido]['titulo']
  nivel_curso = trilha[curso_escolhido]['total_niveis']
  nivel = 1
  
  print ("*" * 50)
  print (f"Bem vindo ao curso de {curso_corrente} ")
  print ("*" * 50)
  while nivel <= nivel_curso:
    print(f'Parabéns você passou do nível {nivel} !!!!')
    nivel += 1
  else:
    print(f'Parabéns você foi aprovado no curso {curso_corrente} !!!!')
# Execute as funções

curso = selecionar_curso()
percorrer_curso(curso)

        