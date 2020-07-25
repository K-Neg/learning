print('Olá, vamos medir as paredes? ')
largura = float(input('Largura da parede = '))
altura = float(input('Altura da parede = '))
area = largura * altura
# 1 litro de tinta pinta 2m2
tinta = area / 2
print('Precisará de {:.4f} litros de tinta'.format(tinta))
