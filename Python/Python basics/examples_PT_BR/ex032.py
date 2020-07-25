ano = int(input('Diga o ano: '))

#regras bissextas

#De 4 em 4 anos é ano bissexto.
#De 100 em 100 anos não é ano bissexto.
#De 400 em 400 anos é ano bissexto.
#Prevalecem as últimas regras sobre as primeiras.

gab = [0,0,0]

if (ano % 400) == 0:
    gab [0] = 1
    print('Ano bissexto')
else:
    if ano % 4 == 0:
        gab[1] = 1
        if ano % 100 != 0:
            gab[2] = 1
            print('Ano bissexto')
        else:
            print('Não é bissexto')
    else:
        print('Não é bissexto')