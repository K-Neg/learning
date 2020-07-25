import pandas as pd

df1 = pd.DataFrame(['a','b','c'],['d','e','f'])#'g','h','i'])

df2 = pd.DataFrame({'nome':['carlos','jovem','dani'],'idade':[24,54,77]})

nomes =['jon','mike','fir']
idades =[24,35,56]
compras=[True,False,True]

labels=['nome','idade','comprou']
list_cols = [nomes,idades,compras]

dados = dict(list(zip(labels,list_cols)))

df3= pd.DataFrame(dados)

print(df3)