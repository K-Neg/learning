distancia = int(input('Distância da viagem: '))
# o valor sera ABC caso ABC se não ABC
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Para uma viagem de {} km o valor é ser pago é '
      'de {:.2f} reais.'.format(distancia, preco))
