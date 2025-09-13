# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
nome = input("digite aqui o seu nome: ")
linkedin = input("quando conheceu o linkedin? ")
ano_atual = input("em que ano estamos?")
cursos_realizados = input("Me fale os cursos realizados até o momento: (Eles precisam ser separados por virgula)")
# 2. Armazene esses dados em um dicionário
estudante = {
'Nome':nome,
'linkedin': linkedin,
'Ano atual': ano_atual,
'Cursos realizados' : cursos_realizados
}
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
print (estudante)
print ("#" * 50)

#primeiro_item = list(meu_dicionario.items())[0]
#primeira_chave = primeiro_item[0]
#primeiro_valor = primeiro_item[1]

#print (primeiro_curso)
#print (ultimo_curso)

#print (f'{nome}, você conheceu o linkedin em {linkedin}. Isso tem {int(ano_atual) - int(linkedin)}! Fantástico, você fez {int(cursos_realizados)} cursos. O primeiro foi {list(cursos_realizados.items())[0]} e o ultimo foi {list(cursos_realizados.items())[-1]}')