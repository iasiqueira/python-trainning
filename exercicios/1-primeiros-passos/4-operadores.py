ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
print ("#" * 20)
idade_gerlaine = 2010 - 1989
print (f"A idade da Gerliane é: {idade_gerlaine}")

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print ("#" * 20)
print (ano_nascimento > ano_formatura)
print (ano_nascimento == ano_formatura)
print (ano_nascimento <= ano_formatura)


# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
resultado1 = 10 == 10 and 3 >10
resultado2 = 10 == 10 or 3 > 10
resultado3 = 10 == 11 or 3 < 10
resultado4 = not (10 == 10)

print ("#" * 20)
print (resultado1)
print (resultado2)
print (resultado3)
print (resultado4)