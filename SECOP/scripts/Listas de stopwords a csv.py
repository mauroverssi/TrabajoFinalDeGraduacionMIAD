# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:09:16 2023

@author: PC
"""

#Acá hay se convierte las stopwords usasas en python a CSV para ser utilizadas en Rstudio

df1= pd.DataFrame(lista_stopwords, columns=['word'])
df2= pd.DataFrame(stoplist, columns=['word'])
df3= pd.DataFrame(departamento_list, columns=['word'])

df1.to_csv('G:/Unidades compartidas/Mau/TrabajoFinalDeGraduacionMIAD/exploratorio/Stopwords/stopwords1.csv', index=False)
df2.to_csv('G:/Unidades compartidas/Mau/TrabajoFinalDeGraduacionMIAD/exploratorio/Stopwords/stopwords2.csv', index=False)
df3.to_csv('G:/Unidades compartidas/Mau/TrabajoFinalDeGraduacionMIAD/exploratorio/Stopwords/stopwords3.csv', index=False)
