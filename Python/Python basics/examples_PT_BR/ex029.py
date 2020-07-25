v_carro = int(input('Velocidade lida pelo radar '))
v_lei = 80
if v_carro > v_lei:
    v_multa = (v_carro - v_lei ) * 7
    print('Multado em {:.2f} reais.'.format(v_multa))
else:
    print('Tudo certo')