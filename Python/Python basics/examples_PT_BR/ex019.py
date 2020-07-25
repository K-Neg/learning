import random
import emoji

print(emoji.emojize("Alguem tera que apagar o quadro :smirk:",use_aliases=True))

n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [ n1, n2, n3, n4]
esc = random.choice(lista)
print("O aluno escolhido foi o ",esc)

