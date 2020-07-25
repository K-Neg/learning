import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import urllib.request
import os
 
# URL com os dados da survey do Stack Overflow
DATA_URL = "https://s3.amazonaws.com/video.udacity-data.com/topher/2018/February/5a8cb654_survey-results-public/survey-results-public.csv"
 
def get_survey_data(data_url=DATA_URL):
    """
    Baixa os dados da survey do Stack Overflow.
 
    Parâmetros:
        data_url &lt;string&gt;: Endereço do arquivo csv com a survey do Stack Overflow
 
    Retorna:
        None
    """
    csv_file = data_url.split(os.sep)[-1]
 
    if not os.path.isfile(csv_file):
        urllib.request.urlretrieve(DATA_URL, 'survey-results-public.csv')
        print("[+] Arquivo baixado...")
 
    else:
        print("[+] O arquivo '{}' já existe na pasta...".format(csv_file))