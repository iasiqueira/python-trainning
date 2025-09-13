# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input("Informe o seu nome: ")
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input("Quantos dias vc se dedicou para estudo essa semana? ")
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input("Quantas horas em media vc se dedicou para estudo essa semana? ")
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input("Qual o curso que vc está se dedicando? ")
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print(f"# Parabéns {nome}, você estudou {total_dias} dias, contabilizando um total de {int(total_dias) * int(total_horas)} horas semanais no curso de {curso}.")