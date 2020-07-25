sal = int(input('Salário '))

if sal > 1250:
    sal = sal*1.1
else:
    sal = sal*1.15

print('O aumento será de {} reais.'.format(sal))
