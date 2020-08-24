#printando um item específico (assim como nas listas)
x = ('Glenn', 'Ren', 'Luka')
print(x[2])
#printando a tupla por inteira
y = (1, 9, 2)
print(y)
#printando o maior (mesmo uso da lista)
print(max(y))
#usando cond. de repetições com tupla
for iter in y:
    print(iter)

#tuplas em dicionários
d = {'a': 10, 'b': 1, 'c': 22}
d.items()
#criando uma cópia dos items sorteados (os itens ficam dentro de tuplas)
t = sorted(d.items())
for k, v in sorted(d.items):
    print(k, v)

#invertendo e organizando um dicionário pela grandeza dos valores
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k)) #invertendo chaves e valores
#organizando os valores por tamanho
tmp = sorted(tmp, reverse=True)
print(tmp)

#programa para saber as 10 palavras mais comuns em um texto
ler = open('romeo.txt')
cont = dict()
for linha in ler:
    palavras = linha.split()
    for palavra in palavras:
        cont[palavra] = cont.get(word, 0) + 1
#criando a lista para organizar os itens
lista = list()
for k, v in cont.items():
    novat = (v, k)
    lista.append(novat)

lista = sorted(lista, reverse=True)

print('10 palavras mais comuns no texto:')
for v, k in lista[:10]:
    print(k, v)

#forma mais simples de fazer o loop das palavras (list comprehension)
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([ (v, k) for k, v in c.items() ])
