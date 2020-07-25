import math
ang = int(input('Qual é o ângulo '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(' '+'_'*12)
print('| Sen = {:.2f} |'.format(sen))
print('| Cos = {:.2f} |'.format(cos))
print('| Tan = {:.2f} |'.format(tan))
print('|'+'_'*12+'|')
