# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 21:28:30 2023

@author: PC
"""
import pandas as pd


#Funciones

def procesar_dataframe(dataframe, nuevos_nombres, nombre_columna):
    # Asignar los nuevos nombres de las columnas al DataFrame
    dataframe.columns = nuevos_nombres
    #Reemplazar las columnas con el primer valor de la fila
    primer_valor = dataframe.iloc[0][nombre_columna]
    dataframe.loc[:, nombre_columna] = primer_valor
    return dataframe

def unir_dataframes(df):
    # Crea los dataframes de cada año
    df_2018 = df.loc[:, ['region', 'variable', '2018']]
    df_2019 = df.loc[:, ['region', 'variable', '2019']]
    df_2020 = df.loc[:, ['region', 'variable', '2020']]
    df_2021 = df.loc[:, ['region', 'variable', '2021']]
    
   

    # Crea los dataframes pivote para cada año
    df_2018_pivot = df_2018.pivot(index='region', columns='variable', values='2018')
    df_2019_pivot = df_2019.pivot(index='region', columns='variable', values='2019')
    df_2020_pivot = df_2020.pivot(index='region', columns='variable', values='2020')
    df_2021_pivot = df_2021.pivot(index='region', columns='variable', values='2021')

     # Agrega el ano
    df_2018_pivot = df_2018_pivot.assign(anio=2018)
    df_2019_pivot = df_2019_pivot.assign(anio=2019)
    df_2020_pivot = df_2020_pivot.assign(anio=2020)
    df_2021_pivot = df_2021_pivot.assign(anio=2021)

    # Une los dataframes pivote
    df_final = pd.concat([df_2018_pivot, df_2019_pivot,  df_2020_pivot,  df_2021_pivot], axis=0)

    # Restablece el índice
    df_final  =df_final .reset_index()
    
    return df_final 
#IPM Regiones
# Ruta al archivo Excel
ruta_archivo = "datos/anexo_dptal_pobreza_multidimensional_21.xls"

# Nombre de la hoja donde están los datos
nombre_hoja = "IPM_Variables_Región"

# Extrear la variables que se necesitan
variables_region_caribe = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(13), nrows=15)
variables_region_oriental = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(38), nrows=15)
variables_region_central = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(63), nrows=15)
variables_region_pacifica = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(88), nrows=15)
variables_region_bogota = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(113), nrows=15)
variables_region_antoquia = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(138), nrows=15)
variables_region_valle_del_cauca = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(163), nrows=15)
variables_region_san_andres = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(189), nrows=15)
variables_region_orinoquia_amazonia = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(214), nrows=15)

nuevos_nombres = ['region', 'variable', '2018', '2019','2020', '2021']
nombre_columna = "region"

variables_region_caribe = procesar_dataframe(variables_region_caribe, nuevos_nombres, nombre_columna)
variables_region_oriental = procesar_dataframe(variables_region_oriental, nuevos_nombres, nombre_columna)
variables_region_central = procesar_dataframe(variables_region_central, nuevos_nombres, nombre_columna)
variables_region_pacifica = procesar_dataframe(variables_region_pacifica, nuevos_nombres, nombre_columna)
variables_region_bogota = procesar_dataframe(variables_region_bogota, nuevos_nombres, nombre_columna)
variables_region_antoquia = procesar_dataframe(variables_region_antoquia, nuevos_nombres, nombre_columna)
variables_region_valle_del_cauca = procesar_dataframe(variables_region_valle_del_cauca, nuevos_nombres, nombre_columna)
variables_region_san_andres = procesar_dataframe(variables_region_san_andres, nuevos_nombres, nombre_columna)
variables_region_orinoquia_amazonia = procesar_dataframe(variables_region_orinoquia_amazonia, nuevos_nombres, nombre_columna)



variables_region_caribe= unir_dataframes(variables_region_caribe)
variables_region_oriental= unir_dataframes(variables_region_oriental)
variables_region_central= unir_dataframes(variables_region_central)
variables_region_pacifica= unir_dataframes(variables_region_pacifica)
variables_region_bogota= unir_dataframes(variables_region_bogota)
variables_region_antoquia= unir_dataframes(variables_region_antoquia)
variables_region_valle_del_cauca= unir_dataframes(variables_region_valle_del_cauca)
variables_region_san_andres= unir_dataframes(variables_region_san_andres)
variables_region_orinoquia_amazonias= unir_dataframes(variables_region_orinoquia_amazonia)



variables_region = pd.concat([variables_region_caribe, variables_region_oriental,
                              variables_region_central, variables_region_pacifica,
                              variables_region_bogota,variables_region_antoquia,
                              variables_region_valle_del_cauca,variables_region_san_andres,
                              variables_region_orinoquia_amazonias], axis=0)


variables_region=variables_region.reset_index()

# Guardar el DataFrame 
variables_region.to_csv('salidas/variables_region.csv', index=False)



























