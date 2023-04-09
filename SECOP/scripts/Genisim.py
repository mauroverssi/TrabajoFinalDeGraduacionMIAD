# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:54:48 2023

@author: PC
"""



#Genisim base. Sin lemantizar

import csv
import pandas as pd
from gensim import corpora

##Función para abrir e iterar el archivo linea por linea

def iter_csv_file(filename, column_name):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row[column_name]
            
#Función para convertir dodo en minuscula y separar en tokens      
def iter_column(df, col_name):
    for line in df[col_name]:
        yield line.lower().split()
  
#Función para crearel corpus  

class MyCorpus():
    
    def iter_csv_file(filename, column_name):
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield row[column_name]
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __iter__(self):
        for line in iter_csv_file('datos/df_secop_obra.csv', 'Detalle_Objeto_Contratar'):
            # assume there's one document per line, tokens separated by whitespace
            yield self.dictionary.doc2bow(line.lower().split())
            
#carga de datos en en un dataframe
datos = pd.read_csv('datos/df_secop_obra.csv',encoding='utf-8')
datos['Detalle_Objeto_Contratar']=datos['Detalle_Objeto_Contratar'].astype(str)
#Pasar la columna Detalle_Objeto_Contratar de object a stream porque sino da un error
dictionary = corpora.Dictionary(iter_column(datos, 'Detalle_Objeto_Contratar'))


#Listado de stopwords
from nltk.corpus import stopwords
lista_stopwords = stopwords.words("spanish")


#Crear los ids de los stopswords
stop_ids = [
    dictionary.token2id[stopword]
    for stopword in lista_stopwords
    if stopword in dictionary.token2id
]

once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.items() if docfreq == 1] #Remover palabras que solo se mencionan 1 vez 
dictionary.filter_tokens(stop_ids + once_ids)  # remove stop words and words that appear only once
dictionary.compactify() #remueve los espacios en las secuencias después de remover las stopswords


corpus= MyCorpus(dictionary)

from gensim.models import LdaModel



Estimacion = LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=10,
    chunksize=1000,
    passes=20,
    iterations=400,
    alpha='auto',
    eta='auto',
    random_state=123,
    eval_every=None
)


from pprint import pprint

pprint(Estimacion.print_topics())


# Visualizamos los resultados
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis


LDA_visualization = gensimvis.prepare(Estimacion, corpus, dictionary)
LDA_visualization


pyLDAvis.show(LDA_visualization)

pyLDAvis.save_html(LDA_visualization, 'lda.HTML')







