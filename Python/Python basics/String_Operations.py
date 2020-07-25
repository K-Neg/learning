frase = 'curso em video'

#exibições
print('') #exibe normalmente
print(""" """) #exibe com quebra de linha


#Fatiamento

frase[9:13] #fatia do string 9 ao 12 (n pega o ultimo)
frase[9:16:2] #fatia o intervalo desejado pulando de 2 em 2
frase[:5] #fatia do começo até o 5 caractere
frase[15:] # fatia do 15 até o fim
frase[9::3] # fatia do 9 até o final, pulando de 3 em 3

#Analise

len(frase) # retorna o tamanho do string
frase.count('o') # conta quantas vezes aparece a letra 'o'
frase.count('o',0,8) #conta dentro do intervalo
frase.find('em') #Procura a combinação 'em' dentro da string , retorna -1 se falso
'Curso' in frase #responde true ou false se possue ou não

#Transformação

frase.replace('video','tenis') #acha e substitui video por tenis
frase.upper() #joga tudo em maiusculas
frase.lower() #joga tudo em minusculas
frase.capitalize() #Primeira letra da frase em maiusculo
frase.title() #Camel Case Em Todas As Palavras
frase.strip() #remove todos os espaços em branco
frase.lstrip() #remove espaços em branco da esquerda
frase.rstrip() #remove espaços em branco da direita

#Divisão

frase.split() #divide a string baseada em seus espaços

#Junção

'-'.join(frase) #une varios string em um unico , separando por -