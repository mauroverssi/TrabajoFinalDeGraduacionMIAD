# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:46:17 2023

@author: PC
"""
import pandas as pd
import nltk

import unidecode
import regex
import spacy
nlp = spacy.load("es_core_news_sm")


from nltk.corpus import stopwords
lista_stopwords = stopwords.words("spanish")

nlp = spacy.load("es_core_news_sm")
nltk.download('stopwords')

datos = pd.read_csv('datos/df_secop_obra.csv')
datos_sample= datos.sample(n=18000, random_state=42)

datos.columns
datos.head()
def text_cleaning(txt):

    out = unidecode.unidecode(txt)
    out = out.split(" ")
    out = [regex.sub("[^\\w\\s]|\n", "", i) for i in out]
    out = [regex.sub("^[0-9]*$", "", i) for i in out]
    out = [ i.lower() for i in out]
    out = [i for i in out if i not in lista_stopwords]
    out = ' '.join(out)
    out = nlp(out)
    out = [x.lemma_ for x in out]
    out = [regex.sub("él", "", i) for i in out]
    out = [i for i in out if len(i) >= 2]
    return out

clean = list(map(text_cleaning, datos_sample['Detalle_Objeto_Contratar']))

txt=datos_sample['Detalle_Objeto_Contratar'].iloc[0]

    out = unidecode.unidecode(txt)
    out = out.split(" ")
    out = [regex.sub("[^\\w\\s]|\n", "", i) for i in out]
    out = [regex.sub("^[0-9]*$", "", i) for i in out]
    out = [ i.lower() for i in out]
    out = [i for i in out if i not in lista_stopwords]
    out = ' '.join(out)
    out = nlp(out)
    out = [x.lemma_ for x in out]
    out = [i for i in out if len(i) >= 2]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    