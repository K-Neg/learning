import emoji
num = int(input('Diga o número -> '))
x = num % 2
if x==1:
    print('O número é impar '+ emoji.emojize(":smirk:",use_aliases=True))
else:
    print('O número é par')

