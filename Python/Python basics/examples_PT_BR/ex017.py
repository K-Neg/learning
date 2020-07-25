import math
cat_adj = int(input('O cateto adjacente '))
cat_op = int(input('O cateto oposto '))
hyp = math.hypot(cat_adj,cat_op)
print('A hypotenusa é {:.2f}'.format(hyp))
