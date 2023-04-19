
library(dplyr)
library(tidytext)
library(stopwords)
library(ggplot2)
library(tidyr)
library(igraph)
library(ggraph)
library(widyr)
library(readr)

#CArga de datos 

datos <- read_csv("G:/Unidades compartidas/Mau/TrabajoFinalDeGraduacionMIAD/SECOP/datos/df_secop_obra.csv")

datos <- datos %>% 
  select(-'...1')%>% 
  mutate(id=row_number())

datos$Detalle_Objeto_Contratar <- tolower(datos$Detalle_Objeto_Contratar)

datos$Detalle_Objeto_Contratar <- chartr("áéíóú","aeiou",datos$Detalle_Objeto_Contratar)

saveRDS(datos, file = "salidas/datos.rds")



