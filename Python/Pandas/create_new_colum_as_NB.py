import pandas as pd

name =['jon','mike','fir']
age =[24,35,56]
double=['','','']

labels=['Name','Age','Double_Age']
list_cols = [name,age,double]

dados = dict(list(zip(labels,list_cols)))

df= pd.DataFrame(dados)


df['Double_Age'] = df['Age'].apply(lambda x: x*2)

invert = df['Double_Age'].copy()
invert.sort_values(ascending = False,inplace=True)
invert.reset_index(drop=True)

print(invert)
df['Inversion']	= invert

print(df)


