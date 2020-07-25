# importar os pacotes necessários
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# importar o arquivo csv em um df
df = pd.read_fwf('FILE.txt', sep=" ", header=None, encoding='utf-8')

text_colum = df[1].astype(str)

# concatenar as palavras
all_summary = " ".join(s for s in text_colum)
all_summary=all_summary.lower()

#print(all_summary)

# lista de stopword
ban = (["da", "meu", "em", "você", "de", "ao", "os"])

#ban = (["media","omitted"])

stops = set(STOPWORDS)
stops.update(ban)

# endereço LOCAL da SUA imagem
#mask1 = np.array(Image.open("f.png"))

# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stops,
                      background_color="black",
 #                     mask = mask1,
                      width=1600, height=800).generate(all_summary)

# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()

plt.imshow(wordcloud);
plt.show()

