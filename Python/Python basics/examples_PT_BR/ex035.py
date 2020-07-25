a = int(input('Primeira reta '))
b = int(input('Segunda reta '))
c = int(input('Terceira reta '))

if a < c + c and b < a +c and c < a +b:
    print('Triângulo real')
else:
    print('Não é triângulo')