# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:19:59 2023

@author: PC
"""

# Librerias

import csv
import pandas as pd
from gensim import corpora

from nltk.corpus import stopwords
lista_stopwords = stopwords.words("spanish")

import spacy

nlp = spacy.load("es_core_news_md")

# Funciones

## Función para abrir e iterar el archivo de los contratos linea por linea

def iter_csv_file(filename, column_name):
    """
    Esta función toma un archivo CSV y el nombre de una columna y devuelve un iterador que
    produce los valores de esa columna para cada fila en el archivo.
    
    Argumentos:
        filename (str): El nombre del archivo CSV a leer.
        column_name (str): El nombre de la columna en la que queremos iterar.
        
    Yields:
        El valor de la columna especificada para cada fila en el archivo.
        
    Ejemplo de uso:
    
    >>> for value in iter_csv_file('datos.csv', 'edad'):
            print(value)
            
        27
        35
        42
        18
        ...
    """
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row[column_name]

## Función para iterar la fila de una columna de un dataframe linea por linea

def iter_dataframe(df, column_name):
    """
    Esta función toma un DataFrame de pandas y el nombre de una columna y devuelve un iterador que
    produce los tokens lematizados para cada fila en la columna especificada.
    
    Argumentos:
        df (pandas.DataFrame): El DataFrame de pandas a leer.
        column_name (str): El nombre de la columna en la que queremos iterar.
        
    Yields:
        Una lista de los tokens lematizados para cada fila en la columna especificada.
        
    """
    for line in df[column_name]:
        # Se remueven las stopwords y las palabras que aparecen solo una vez antes de aplicar la lematización
        doc = [token for token in nlp(line.lower()) if token.text not in lista_stopwords]
        yield [token.lemma_ for token in doc]

 
## Función para iterar una columna y devolver una lista de lemas
           
def iter_column(df, col_name):
    """
    Esta función toma un DataFrame de pandas y el nombre de una columna y devuelve un iterador que
    produce una lista de lemas para cada línea en la columna especificada.
    
    Argumentos:
        df (pandas.DataFrame): El DataFrame de pandas a leer.
        col_name (str): El nombre de la columna en la que queremos iterar.
        
    Yields:
        Una lista de lemas para cada línea en la columna especificada.
        
    Ejemplo de uso:
    
    >>> for lemmas in iter_column(df, 'texto'):
            print(lemmas)
            
        ['comprar', 'manzana', 'pera', 'naranja']
        ['ir', 'cine', 'amigo']
        ['cocinar', 'comida', 'saludable', 'cena']
        ...
    """
    # Itera sobre cada línea en la columna especificada
    for line in df[col_name]:
        # Se remueven las stopwords y las palabras que aparecen solo una vez antes de aplicar la lematización
        doc = [token for token in nlp(line.lower()) if token.text not in lista_stopwords]
        # Itera sobre cada token en el objeto Doc y devuelve su forma lematizada utilizando el atributo lemma_
        lemmas = [token.lemma_ for token in doc]
        # Genera una lista de lemas para cada línea en la columna de entrada utilizando la sentencia yield
        yield lemmas

  
## Función para crear el corpus a partir de todos los datos

class MyCorpus():
    """
    Esta clase es una implementación de la interfaz de corpus de Gensim, que define cómo se accede a los documentos en un corpus de texto.
    """
                
    # Constructor de la clase MyCorpus
    def __init__(self, dictionary):
        """
        Constructor de la clase MyCorpus.
        
        Argumentos:
        dictionary (gensim.corpora.Dictionary): Objeto de diccionario de Gensim que se utilizará para crear bolsas de palabras.
        """
        self.dictionary = dictionary

    # Método que devuelve un generador que produce bolsas de palabras para cada línea en el archivo CSV
    def __iter__(self):
        """
        Método que devuelve un generador que produce bolsas de palabras para cada línea en el archivo CSV.
        
        Yields:
        Una bolsa de palabras para cada línea en el archivo CSV.
        """
        # Itera sobre cada línea en el archivo CSV utilizando el método iter_csv_file
        for line in iter_csv_file('datos/df_secop_obra.csv', 'Detalle_Objeto_Contratar'):
            # Convierte la lista de lemas en una bolsa de palabras utilizando el método doc2bow de self.dictionary
            yield self.dictionary.doc2bow(line.split())


# Función para crear el corpus a partir de la muestra
class MyCorpus_sample():
    """
    Esta clase es una implementación de la interfaz de corpus de Gensim, que define cómo se accede a los documentos en un corpus de texto.
    """
                
    # Constructor de la clase MyCorpus
    def __init__(self, dictionary, df, column_name):
        """
        Constructor de la clase MyCorpus.
        
        Argumentos:
        dictionary (gensim.corpora.Dictionary): Objeto de diccionario de Gensim que se utilizará para crear bolsas de palabras.
        df (pandas.DataFrame): El DataFrame de pandas a leer.
        column_name (str): El nombre de la columna en el que queremos iterar.
        """
        self.dictionary = dictionary
        self.df = df
        self.column_name = column_name

    # Método que devuelve un generador que produce bolsas de palabras para cada línea en el dataframe
    def __iter__(self):
        """
        Método que devuelve un generador que produce bolsas de palabras para cada línea en el dataframe.
        
        Yields:
        Una bolsa de palabras para cada línea en el dataframe.
        """
        # Itera sobre cada línea en el dataframe utilizando el método iter_dataframe
        for line in iter_dataframe(self.df, self.column_name):
            # Convierte la lista de lemas en una bolsa de palabras utilizando el método doc2bow de self.dictionary
            yield self.dictionary.doc2bow(' '.join(line).split())


# Carga de datos

## Carga de datos en en un dataframe
datos = pd.read_csv('datos/df_secop_obra.csv',encoding='utf-8')


## Pasar la columna Detalle_Objeto_Contratar de object a string porque sino da un error
datos['Detalle_Objeto_Contratar']=datos['Detalle_Objeto_Contratar'].astype(str)

## Crear la muestra
datos_sample= datos.sample(n=18000, random_state=42)

## Crear el diccionario con la muestra

dictionary = corpora.Dictionary(iter_column(datos_sample, 'Detalle_Objeto_Contratar'))

## Crear corpus con l amuestra
corpus_sample= MyCorpus_sample(dictionary, datos_sample,'Detalle_Objeto_Contratar' )




from gensim.models import LdaModel



Estimacion = LdaModel(
    corpus=corpus_sample,
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


LDA_visualization = gensimvis.prepare(Estimacion, list(corpus_sample), dictionary)



pyLDAvis.show(LDA_visualization)

pyLDAvis.save_html(LDA_visualization, 'lda.HTML')







