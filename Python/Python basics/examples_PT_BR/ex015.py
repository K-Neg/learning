dias = int(input('Quantos dias com o carro ? '))
km = float(input('Quantos Km rodados ? '))
# R$60 por dia e R$0,15 por km rodado
total = dias * 60 + km * 0.15
print('O total a pagar é R${:.2f}'.format(total))
