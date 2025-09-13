resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela a variável "resumo"
print ("1 - Imprima na tela a variável ""resumo"":", resumo)

# Imprima na tela apenas a segunda letra da variável
print("2 - Imprima na tela apenas a segunda letra da variável:", resumo[1])

# Imprima na tela a idade de Paloma (resposta esperada: "46")
idade = resumo[23:25]
print ("3 - Imprima na tela a idade de Paloma:",idade)

# Imprima na tela o trecho final da variável
print ("4 - Imprima na tela o trecho final da variável:", resumo[62:])

# Converta todos as letras para minúsculo e imprima na tela
print ("5 - Converta todos as letras para minúsculo e imprima na tela: ", resumo.lower())

# Converta todas as letras para maiúscula e imprima na tela
print ("6 - Converta todos as letras para minúsculo e imprima na tela: ", resumo.upper())

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela
print ("7 - Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela: ", resumo.title())

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela
print ("8 - Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela: ", resumo.capitalize())

# Imprima na tela uma string utilizando uma variável, usando o recurso string format

print ("9 - Imprima na tela uma string utilizando uma variável, usando o recurso string format: ")
print(f"Paloma é uma mulher de {idade} anos que deseja mudar de profissão, por isso está estudando 'python'.")
