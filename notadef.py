def computarnotas(nota):
    if nota > 1 or nota < 0:
      nota = 'Nota inválida.'
    elif nota >= 0.9:
      nota = 'A'
    elif nota >= 0.8:
      nota = 'B'
    elif nota >= 0.7:
      nota = 'C'
    elif nota >= 0.6:
      nota = 'D'
    elif nota < 0.6:
      nota = 'F'
    return nota
try:
    n1 = float(input('Nota: '))
except:
    print('Nota inválida.')

try:
    print(f'A nota final do aluno é {computarnotas(n1)}.')
except:
    n1 = 0
