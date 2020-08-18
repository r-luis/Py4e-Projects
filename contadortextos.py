nome = input('Digite o nome do arquivo: ')
abre = open(nome)
#fazendo a contagem das palavras e adicionando ao dicionario
cont = dict()
for linha in abre:
    palavras = linha.split()
    for palavra in palavras:
        cont[palavra] = cont.get(palavra, 0) + 1

maiorcont = None
maiorpalavra = None
for palavra, contador in cont.items():
    if maiorcont is None or contador > maiorcont:
        maiorpalavra = palavra
        maiorcont = contador

print(f'A palavra com maior uso no texto é `{maiorpalavra}`, usado {maiorcont} vezes.')
