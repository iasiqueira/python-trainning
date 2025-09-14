# Crie duas variáveis do tipo numérica, uma sinalizando a fase atual do curso e outra o nível final
print ("*" * 50)
nivel_atual = 1
nivel_final = 10

# Crie um while loop que imprima na tela o nível atual
while nivel_atual <= nivel_final:
    print(f"Nivel atual é: {nivel_atual}")
    nivel_atual += 1
print("Loop finalizado.")

# Insira "else" no while loop anterior.
print ("*" * 50)

while nivel_atual <= nivel_final:
  print(f"Nivel atual é: {nivel_atual}")
  nivel_atual += 1
else:
  print("Parabens, curso concluido.")

