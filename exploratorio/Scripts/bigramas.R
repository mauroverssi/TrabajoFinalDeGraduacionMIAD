



source("G:/Unidades compartidas/Analytics/Scripts generales/Paleta de colores gráficos/Paleta de colores Banco Nacional.R")
datos <- readRDS("G:/Unidades compartidas/Mau/TrabajoFinalDeGraduacionMIAD/exploratorio/salidas/datos.rds")
load("G:/Unidades compartidas/Mau/TrabajoFinalDeGraduacionMIAD/exploratorio/salidas/stopwords.RData")


bigramas <-datos %>%
  unnest_tokens(bigram, Detalle_Objeto_Contratar, token = "ngrams", n = 2)%>%
  separate(bigram, c("word1", "word2"), sep=" ")

bigramas <-bigramas %>%
  filter(!word1 %in% stopwords1$word) %>%
  filter(!word2 %in% stopwords1$word) %>%
  filter(!word1 %in% stopwords2$word) %>%
  filter(!word2 %in% stopwords2$word) %>%
  filter(!word1 %in% stopwords3$word) %>%
  filter(!word2 %in% stopwords3$word) %>%
  slice(-c(1))%>%
  count(word1, word2, sort = TRUE)


#Bigramas mas frecuentes
#Bigramas más  frecuentes

bigramas %>%
  unite(bigram, word1, word2, sep = " ")%>%
  slice(-c(1))%>%
  filter(n >=1500) %>%
  mutate(pct = prop.table(n))%>%
  mutate(bigram = reorder(bigram, n)) %>%
  ggplot(aes(bigram, n,fill=n)) +
  geom_col() +
  geom_text(
    aes(y=50,label = scales::percent(round(pct,3)))
    , colour="white")+
  coord_flip()+
  ylab("Frecuencia")+
  xlab("Bigramas más frecuentes (n >= 1.500 menciones)")+
  escala_fill_bn(paleta = "logo", guide = "none", discrete =FALSE)

bigramas %>%
  filter(n >= 1000) %>%
  graph_from_data_frame() %>%
  ggraph( layout = "fr") +
  geom_edge_link() +
  geom_node_point() +
  geom_node_text(aes(label = name), vjust = 1, hjust = 1)

a <- grid::arrow(type = "closed", length = unit(.15, "inches"))
bigramas %>%
  slice(-c(1))%>%
  filter(n >= 1000) %>%
  graph_from_data_frame() %>%
  ggraph( layout = "fr") +
  geom_edge_link(aes(edge_alpha = n), show.legend = FALSE,
                 arrow = a, end_cap = circle(.07, 'inches'), color = "blue") +
  geom_node_point(color = "blue", size = 2) +
  geom_node_text(aes(label = name), vjust = 1, hjust = 1) +
  theme_void()

