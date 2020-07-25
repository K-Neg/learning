#https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html


import pandas as pd

#df = pd.read_csv("http://data.insideairbnb.com/turkey/marmara/istanbul/2020-03-22/data/listings.csv.gz")
#df = pd.read_excel("")

#df.shape[0] #linhas
#df.shape[1] #colunas
#df.head()
#df.tail()
#df.info()
#df.COLUNA.unique()
#df.COLUNA.value_counts()	
#type(df)
#tyoe(df['nome da coluna'])


# initialize list of lists 
data = [['tom', 10], ['nick', 15], ['juli', 14]] 
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['Name', 'Age']) 



#Pandas dataframe is like two or more Pandas Series

list_1 = ['m','n','o']
series_1 = pd.Series(list_1,index=[0,1,2])

list_2 = ['p','q','r']
series_2 = pd.Series(list_2,index=[0,1,3])

#Soma simples (estilo escalar)
df = series_1 + series_2

#Concatena
#axis determina se os dados seram colocadas abaixo ou do lado
#join: inner = interseccao , outer = all
df = pd.concat([series_1,series_2],axis=1,join='inner')

df.columns=['A','B']



#Append
#inserir uma nova linha
#sort pode reordenar o df baseando no index

list3 = [{
	'A':'x',
	'B':'y'
	}]

print(list3)

df=df.append(list3,ignore_index=True,sort=False)

print(df)
#df = pd.DataFrame(['a','b','c'],['d','e','f'])#'g','h','i'])

#df = pd.DataFrame({'nome':['carlos','jovem','dani'],'idade':[24,54,77]})

dados = {
    'nome': ['Carlos', 'Pedro', 'Daniela', 'Fernanda'],
    'idade': [35, 32, 15, 49],
    'cidade': ['Araraquara', 'Belém', 'Natal', 'Curitiba'],
    'comprou': [True, False, False, True]
}

nomes =['jon','mike','fir']
idades =[24,35,56]
compras=[True,False,True]

labels=['nome','idade','comprou']
list_cols = [nomes,idades,compras]

dados = dict(list(zip(labels,list_cols)))

df= pd.DataFrame(dados)

#adicionar uma nova coluna
df['EXTRA'] = ['oi',54,'rojo']

#index

#index pode ser chamado diretamente como objeto
df.index

#resetar - n pode usar inplace
#o drop como parametro evita q o antigo index seja add como coluna
cep = cep.reset_index()

#index pode ser alterado como uma lista 
df.index = ['Client A','Lord B','Baker C']

#index alterado mediante uma coluna
df.index =df['nome']

#columns

#exibe nome (label) das colunas
df.columns



df.columns = ['Name','Age','Bought?','Extra']

df.describe() #resumo estatistico

# LINHA
# eliminar todas as entradas onde existam valores ausentes em `user_gender`
#df_row_dropna = df.dropna(subset=['user_gender'], axis=0)

# preencher valores ausentes em `ride_duration` com a mediana
#ride_duration_median = df.ride_duration.median()
#df.ride_duration.fillna(ride_duration_median, inplace=True)

# ver valores ausentes
#df.ride_duration.isnull().sum()


#em grandes DF acaba reduzindo o tempo de processamento
#corta todas as 100% NaN 
df_temp.dropna(axis=1,how='all',inplace=True)
df_temp.dropna(axis=0,how='all',inplace=True)


#graficos direto com panda
#df['Coletor'].plot()
#df['Temp'].hist()
#df.plot.scatter('Temp','Coletor')
#df_clean.Coletor.plot(kind="box")

#LOC
df.loc[(df['ds'] > '2015-06-01') & (df['ds'] < '2015-06-30'), 'y'] = None
df.loc[a_linha_INT_carai, ['col fulano', 'col 2']]

df.loc[df["casos-confirmados"] < 150].boxplot(['casos-confirmados'], vert=False, ax=ax)

#multiplicar ou replicar ou matematica coluna
df['Double_Age'] = df['Age'].apply(lambda x: x*2)

print("\nFraudes representam {:.4f}% do dataset.\n".format((df[df.Class == 1].shape[0] / df.shape[0]) * 100))

print(df)