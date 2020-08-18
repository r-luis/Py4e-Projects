#lendo textos e descobrindo a palavra mais usada
cont = dict()
print('Digite uma linha de texto:')
linha = input('')
palavras = linha.split()

print(f'Palavras: {palavras}')

print('Contando')
for palavra in palavras:
    cont[palavra] = cont.get(palavra, 0) + 1
print(f'Contador: {cont}')

cont = {'ren': 1, 'john': 42, 'supermax': 100}
for key in cont:
    print(key, cont[key])

cont = {'ren': 1, 'john': 42, 'supermax': 100}
for a, b in cont.items(): #usando duas variáveis no for
    print(a, b)
