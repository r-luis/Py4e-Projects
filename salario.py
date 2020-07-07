while True:
    try:
        hrs = float(input('Horas Trabalhadas: '))
        taxa = float(input('Taxa por hora trabalhada: '))
        break
    except:
        print('Precisa ser digitado como NUMERAL. Tente novamente.')
        print('-'*50)

print('-'*50)

if hrs > 40:
    salario = hrs * taxa
    extra = (hrs - 40) * (taxa * 0.5)
    final = salario + extra
    print(f'Salário final: {final}. Sendo:\nR${salario} normal + R${extra} de bônus por hora extra.')
else:
    salario = hrs * taxa
    print(f'Salário final: R${salario}')

print('Obrigado por usar o programa. Volte sempre.')
