# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
nome = input("digite aqui o seu nome: ")
linkedin = input("quando conheceu o linkedin? ")
ano_atual = input("em que ano estamos? ")
cursos_realizados = input("Me fale os cursos realizados até o momento: (Eles precisam ser separados por virgula)")
# 2. Armazene esses dados em um dicionário
estudante = {
'Nome':nome,
'Linkedin': linkedin,
'Ano atual': ano_atual,
'Cursos' : cursos_realizados.split(', ')
}
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
#print (estudante)
print ("#" * 50)
primeiro_curso = estudante["Cursos"][0]
ultimo_curso = estudante["Cursos"][-1]
print (f'{estudante["Nome"]}, você conheceu o linkedin em {estudante["Linkedin"]}. Isso tem {int(estudante["Ano atual"]) - int(estudante["Linkedin"])} anos! Fantástico, você fez {len(estudante["Cursos"])} cursos. O primeiro foi {primeiro_curso} e o ultimo foi {ultimo_curso}')