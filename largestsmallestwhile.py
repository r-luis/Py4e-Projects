maior = None
menor = None
cont = 0

while True:
    entr = input('Digite algum número, ou fim para finalizar: ')

    if entr == 'fim': break

    try:
        int(entr)
    except:
        print('Erro de entrada')
        continue #retorna ao começo do input

    if menor is None:
        menor = entr
    elif maior is None:
        maior = entr
    elif entr >= maior:
        maior = entr
    elif entr <= menor:
        menor = entr

    cont += 1

if cont == 2:
  print(f'O maior número é {menor}.')
  print(f'O menor número é {maior}.')
elif cont != 2:
  print(f'O maior número é {maior}.')
  print(f'O menor número é {menor}.')
