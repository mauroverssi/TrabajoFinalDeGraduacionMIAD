0# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 16:40:24 2023

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

nlp = spacy.load("es_core_news_md")
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
    out = [i for i in out if len(i) >= 2]
    return out

clean = list(map(text_cleaning, datos_sample['Detalle_Objeto_Contratar']))


from gensim.corpora import Dictionary

dictionary = Dictionary(clean)
dictionary

dictionary.filter_extremes(no_below=20, no_above=0.5)

corpus1 = [dictionary.doc2bow(doc) for doc in clean]


print('Numero de palabras únicas: %d' % len(dictionary))



from gensim.models import LdaModel



Estimacion = LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=3,
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







