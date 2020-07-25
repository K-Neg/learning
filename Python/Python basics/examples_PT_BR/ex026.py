#contar as letras A

frase = str(input("Digite a frase ")).strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A letra A aparece primeiro na posição {}'.format(frase.find('a')+1))
print('A letra A aparece por último na posição {}'.format(frase.rfind('a')+1))