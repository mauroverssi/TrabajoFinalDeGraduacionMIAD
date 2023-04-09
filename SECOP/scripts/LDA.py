# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:47:07 2023

@author: PC
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:54:48 2023

@author: PC
"""





import csv
import pandas as pd
from gensim import corpora

import spacy

nlp = spacy.load("es_core_news_md")

##Función para abrir e iterar el archivo de los contratos linea por linea

def iter_csv_file(filename, column_name):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row[column_name]
            
#Función que extraer cada linea del la columna, la       
def iter_column(df, col_name):
    # Itera sobre cada línea en la columna especificada
    for line in df[col_name]:
        # Procesa la línea en minúsculas utilizando el objeto nlp de spacy
        doc = nlp(line.lower())
        # Itera sobre cada token en el objeto Doc y devuelve su forma lematizada utilizando el atributo lemma_
        lemmas = [token.lemma_ for token in doc]
        # Genera una lista de lemas para cada línea en la columna de entrada utilizando la sentencia yield
        yield lemmas
  
#Crear el corpuys  

class MyCorpus():
    # Función para iterar sobre un archivo CSV y devolver una lista de lemas para cada línea en una columna específica
    def iter_csv_file(filename, column_name):
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                doc = nlp(row[column_name].lower())
                yield [token.lemma_ for token in doc]
                
    # Constructor de la clase MyCorpus
    def __init__(self, dictionary):
        self.dictionary = dictionary

    # Método que devuelve un generador que produce bolsas de palabras para cada línea en el archivo CSV
    def __iter__(self):
        # Itera sobre cada línea en el archivo CSV utilizando el método iter_csv_file
        for line in iter_csv_file('datos/df_secop_obra.csv', 'Detalle_Objeto_Contratar'):
            # Convierte la lista de lemas en una bolsa de palabras utilizando el método doc2bow de self.dictionary
            yield self.dictionary.doc2bow(line)
            
#carga de datos en en un dataframe
datos = pd.read_csv('datos/df_secop_obra.csv',encoding='utf-8')
#Pasar la columna Detalle_Objeto_Contratar de object a string porque sino da un error
datos['Detalle_Objeto_Contratar']=datos['Detalle_Objeto_Contratar'].astype(str)

#Crear el diccionario

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







