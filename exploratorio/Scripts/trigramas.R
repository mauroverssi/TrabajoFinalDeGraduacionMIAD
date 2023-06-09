

source("G:/Unidades compartidas/Analytics/Scripts generales/Paleta de colores gráficos/Paleta de colores Banco Nacional.R")
datos <- readRDS("G:/Unidades compartidas/Mau/TrabajoFinalDeGraduacionMIAD/exploratorio/salidas/datos.rds")
load("G:/Unidades compartidas/Mau/TrabajoFinalDeGraduacionMIAD/exploratorio/salidas/stopwords.RData")


trigramas <-datos %>%
  unnest_tokens(trigram, Detalle_Objeto_Contratar, token = "ngrams", n = 3)%>%
  separate(trigram, c("word1", "word2",'word3'), sep=" ")

trigramas <-trigramas %>%
  filter(!word1 %in% stopwords1$word) %>%
  filter(!word2 %in% stopwords1$word) %>%
  filter(!word3 %in% stopwords1$word) %>%
  filter(!word1 %in% stopwords2$word) %>%
  filter(!word2 %in% stopwords2$word) %>%
  filter(!word3 %in% stopwords2$word) %>%
  filter(!word1 %in% stopwords3$word) %>%
  filter(!word2 %in% stopwords3$word) %>%
  filter(!word3 %in% stopwords3$word) %>%
  slice(-c(1))%>%
  count(word1, word2,word3, sort = TRUE)


#Bigramas mas frecuentes
#Bigramas más  frecuentes

trigramas %>%
  unite(trigram, word1, word2,word3, sep = " ")%>%
  slice(-c(1))%>%
  filter(n >=300) %>%
  mutate(pct = prop.table(n))%>%
  mutate(trigram = reorder(trigram, n)) %>%
  ggplot(aes(trigram, n,fill=n)) +
  geom_col() +
  geom_text(
    aes(y=50,label = scales::percent(round(pct,3)))
    , colour="white")+
  coord_flip()+
  ylab("Frecuencia")+
  xlab("Trigramas más frecuentes (n >= 300 menciones)")+
  escala_fill_bn(paleta = "logo", guide = "none", discrete =FALSE)

trigramas %>%
  filter(n >= 300) %>%
  graph_from_data_frame() %>%
  ggraph( layout = "fr") +
  geom_edge_link() +
  geom_node_point() +
  geom_node_text(aes(label = name), vjust = 1, hjust = 1)

a <- grid::arrow(type = "closed", length = unit(.15, "inches"))
trigramas %>%
  slice(-c(1))%>%
  filter(n >= 200) %>%
  graph_from_data_frame() %>%
  ggraph( layout = "fr") +
  geom_edge_link(aes(edge_alpha = n), show.legend = FALSE,
                 arrow = a, end_cap = circle(.07, 'inches'), color = "blue") +
  geom_node_point(color = "blue", size = 2) +
  geom_node_text(aes(label = name), vjust = 1, hjust = 1) +
  theme_void()

library(igraph)
library(tidyverse)

# Crear un grafo vacío
g <- graph.empty(n = 0, directed = TRUE)

# Agregar los nodos y aristas
for (i in 1:nrow(trigramas)) {
  g <- g + vertices(trigramas$word1[i]) + vertices(trigramas$word2[i]) + vertices(trigramas$word3[i])
  g <- g + path(trigramas$word1[i], trigramas$word2[i], trigramas$word3[i], edge.attr = list(weight = trigramas$n[i]))
}

# Eliminar duplicados de vértices
g <- simplify(g, remove.multiple = FALSE, edge.attr.comb = "sum")
