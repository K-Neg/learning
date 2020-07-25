import random
y = int(input('Adivinha o número (1 a 5): '))
x = int(random.choice('12345'))
#pode usar: ranint(0,5)
if x==y:
    print( 'Parabéns! Você acertou.')
else:
    print('Não foi dessa vez.' )
print( 'Parabéns! Você acertou.' if x==y else 'Não foi dessa vez.')
print(x)
print(y)
