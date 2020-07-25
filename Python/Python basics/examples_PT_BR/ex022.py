frase = input('Nome ')
print('O Nome é {}'.format(frase))
print('O nome em maiusculo {}'.format(frase.upper()))
print('O nome em maiusculo {}'.format(frase.lower()))
#remove os espaços no começo e final
frase.strip
#localiza a divisao de palavra (se tiver)
x = frase.find(' ')
#separa o primeiro nome
frase_cut = frase[:x]
nc = len(frase_cut)
n = len(frase)
print('O nome possue {} caracteres'.format(n))
print('O primeiro nome possue {} caracteres'.format(nc))



