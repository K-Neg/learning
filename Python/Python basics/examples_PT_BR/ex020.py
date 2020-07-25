import random
import emoji

print(emoji.emojize("Vamos sortear a sequência de apresentação: smirk:",use_aliases=True))

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [ n1, n2, n3, n4]
random.shuffle(lista)
print("A sequência de apresentação é ")
print(lista)



