num = [0,0,0]
i = 0
num[i] = int(input('Primeiro número '))
maior = num[i]
menor = num[i]
i = i + 1
num[i] = int(input('Segundo número '))
if num[i] > maior: maior = num[i]
if num[i] < menor: menor = num[i]
i = i +1
num[i] = int(input('Terceiro número '))
if num[i] > maior: maior = num[i]
if num[i] < menor: menor = num[i]
print('')
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))

