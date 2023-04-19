
library(tidyverse)
library(readr)
library(paletteer)
library(scales)
library(ggplot2)

datos <- readRDS("G:/Unidades compartidas/Mau/TrabajoFinalDeGraduacionMIAD/exploratorio/salidas/datos.rds")



source("G:/Unidades compartidas/Analytics/Scripts generales/Paleta de colores gráficos/Paleta de colores Banco Nacional.R")
#Tokens

detalle_contrato<-datos%>%
  unnest_tokens(word,Detalle_Objeto_Contratar)


stopwords1 <- read_csv("Stopwords/stopwords1.csv")
stopwords2 <- read_csv("Stopwords/stopwords2.csv")
stopwords3 <- read_csv("Stopwords/stopwords3.csv")


#Quitar mínusculas y acentos


detalle_contrato <- detalle_contrato %>% 
  anti_join(stopwords1)%>% 
  anti_join(stopwords2)%>%
  anti_join(stopwords3)
#Graficar palabras más comunes#
detalle_contrato %>%
  count(word, sort = TRUE) %>%
  filter(n > 10000) %>%
  mutate(pct = prop.table(n))%>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n,fill=n)) +
  geom_col() +
  geom_text(
    aes(y=200,label = scales::percent(round(pct,2)))
    , colour="white")+
  coord_flip()+
  ylab("Frecuencia")+
  xlab("Top de Palabras más frecuentes (>=10.000 menciones)")+
  escala_fill_bn(paleta = "logo", guide = "none", discrete =FALSE)

save(stopwords1,stopwords2,stopwords3, file = "salidas/stopwords.RData")
