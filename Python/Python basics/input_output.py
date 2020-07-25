print("Olá Mundo!")

nome = input("Qual teu nome? ")
print(nome)
print("Oi {}, seja bem vindo!".format(nome))

#varias entradas de uma vez só

name, age, phone = input("Enter your name, Age, Percentage separated by space: ").split()
print("User Details: ", name, age, phone)

#######

dia = input("Dia de nascimento: ")
mes = input("Mes de nascimento: ")
ano = input("Ano de nascimento: ")
print("Você nasceu no dia " + dia + " de " + mes + " de " + ano)

numero = float(input('QUAL É O NÚMERO -->'))
print('Sucessor = ', numero + 1)
print('Antecessor = ', numero -1)

numero = float(input('Qual é o número --> '))
print('Seu dobro = ', numero*2)
print('Seu triplo = ', numero*3)
print('Sua raiz quadrada = ', numero**(1/2))

n1 = float(input('A nota 1: '))
n2 = float(input('A nota 2: '))
media = (n1+n2) /2
print('A média do aluno é: {:.2f}'.format(media))

metros = float(input('Tamanho em metros --> '))
print('Mesmo tamanho em CM: ', metros * 100)
print('Mesmo tamanho em MM: ', metros * 1000)

dinheiro = float(input('Qual tua grana?   > '))
## 1 dol = 3,27 reais
dol = 3.27
print('Da pra comprar {:.6f} dolares'.format( dinheiro / dol))


numero = int(input('Seu numero: '))
i = 0
print('{} X {} = {}'.format(numero, i, numero * i))
i = i + 1
print('{} X {} = {}'.format(numero, i, numero * i))
i = i + 1
print('{} X {} = {}'.format(numero, i, numero * i))
i = i + 1
print('{} X {} = {}'.format(numero, i, numero * i))
i = i + 1
print('{} X {} = {}'.format(numero, i, numero * i))
i = i + 1
print('{} X {} = {}'.format(numero, i, numero * i))
i = i + 1
print('{} X {} = {}'.format(numero, i, numero * i))
i = i + 1
print('{} X {} = {}'.format(numero, i, numero * i))
i = i + 1
print('{} X {} = {}'.format(numero, i, numero * i))
i = i + 1
print('{} X {} = {}'.format(numero, i, numero * i))
i = i + 1
print('{} X {} = {}'.format(numero, i, numero * i))
i = i + 1


print('Olá, vamos medir as paredes? ')
largura = float(input('Largura da parede = '))
altura = float(input('Altura da parede = '))
area = largura * altura
# 1 litro de tinta pinta 2m2
tinta = area / 2
print('Precisará de {:.4f} litros de tinta'.format(tinta))


preco_inicial = float(input('Preço inicial : '))
preco_final = preco_inicial * 0.95
print('O preço final do produto é {:.2f}'.format(preco_final))


print('Seja bem vindo')
sal_i = float(input('Salário atual: '))
print('Seu aumento: ', sal_i * 0.05)
print('Teu salário final: ', sal_i * 1.05)


c = float(input('Informe a temperatura em Cº -> '))
f = ((9*c)/5)+32
print('A temperatura de {:.4f}ºC equivale a {:.4f}ºF'.format(c, f))


dias = int(input('Quantos dias com o carro ? '))
km = float(input('Quantos Km rodados ? '))
# R$60 por dia e R$0,15 por km rodado
total = dias * 60 + km * 0.15
print('O total a pagar é R${:.2f}'.format(total))


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




