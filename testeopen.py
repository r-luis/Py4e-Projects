texto = open('tarefas.txt')
cont = 0

for linha in texto:
  cont += 1

print(f'Linhas do texto: {cont}')
