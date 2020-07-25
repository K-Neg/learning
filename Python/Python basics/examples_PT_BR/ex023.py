num = int(input('Qual o número '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 10 % 10
m = num // 1000 % 10

print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))