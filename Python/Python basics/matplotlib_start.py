import matplotlib.pyplot as plt
import numpy as np

x1 = [1,3,5,7,9]
y1 = [2,4,1,6,8]

x2 = [0,2,4,6,8]
y2 = [1,2,3,4,5]

z2 = [3,6,1,9,11]

y3 = np.array(y1)
y3 = y3 +1 


titulo = "grafico de barras"
eixox = "eixo x"
eixoy = "eixo y"

#titulo
plt.title(titulo)

#Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

#gera e exibe
plt.bar(x1,y1,label = "Grupo 1")
plt.bar(x2,y1,label = "Grupo 2")
plt.plot(z2,y1,label = "Grupo 5", color = 'k',linestyle = 'dashed')
plt.scatter(y1,y3,label = "Grupo 1",color = 'green')
plt.legend()
plt.show()