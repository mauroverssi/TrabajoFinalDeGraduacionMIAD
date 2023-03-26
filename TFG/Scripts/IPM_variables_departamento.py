# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:20:41 2023

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

def reordenar_dataframes(df):
    # Crea los dataframes de cada año
    df_2018 = df.iloc[:, :5]
    df_2019 = df.iloc[:, [0, 1, 5, 6, 7]]
    df_2020 = df.iloc[:, [0, 1, 8, 9, 10]]
    df_2021 = df.iloc[:, [0, 1, 11, 12, 13]]

    nuevos_nombres_2 = ['departamento', 'variable', 'total', 'cabeceras', 'centros_poblados_rural_disperso']
    
    df_2019.columns = nuevos_nombres_2
    df_2020.columns = nuevos_nombres_2
    df_2021.columns = nuevos_nombres_2
    

    #Separar por tipos
    
    df_2018t = df_2018.iloc[:, :3]
    df_2018c = df_2018.iloc[:,[0,1,3]]
    df_2018cp = df_2018.iloc[:,[0,1,4]]
    
    df_2019t = df_2019.iloc[:, :3]
    df_2019c = df_2019.iloc[:,[0,1,3]]
    df_2019cp = df_2019.iloc[:,[0,1,4]]
    
    df_2020t = df_2020.iloc[:, :3]
    df_2020c = df_2020.iloc[:,[0,1,3]]
    df_2020cp = df_2020.iloc[:,[0,1,4]]
    
    df_2021t = df_2021.iloc[:, :3]
    df_2021c = df_2021.iloc[:,[0,1,3]]
    df_2021cp = df_2021.iloc[:,[0,1,4]]

#Pivote

    df_2018t_pivot = df_2018t.pivot(index='departamento', columns='variable', values='total')
    df_2018c_pivot = df_2018c.pivot(index='departamento', columns='variable', values='cabeceras')
    df_2018cp_pivot = df_2018cp.pivot(index='departamento', columns='variable', values='centros_poblados_rural_disperso')


    df_2019t_pivot = df_2019t.pivot(index='departamento', columns='variable', values='total')
    df_2019c_pivot = df_2019c.pivot(index='departamento', columns='variable', values='cabeceras')
    df_2019cp_pivot = df_2019cp.pivot(index='departamento', columns='variable', values='centros_poblados_rural_disperso')

    df_2020t_pivot = df_2020t.pivot(index='departamento', columns='variable', values='total')
    df_2020c_pivot = df_2020c.pivot(index='departamento', columns='variable', values='cabeceras')
    df_2020cp_pivot = df_2020cp.pivot(index='departamento', columns='variable', values='centros_poblados_rural_disperso')


    df_2021t_pivot = df_2021t.pivot(index='departamento', columns='variable', values='total')
    df_2021c_pivot = df_2021c.pivot(index='departamento', columns='variable', values='cabeceras')
    df_2021cp_pivot = df_2021cp.pivot(index='departamento', columns='variable', values='centros_poblados_rural_disperso')


    df_2018t_pivot = df_2018t_pivot.assign(tipo="total")
    df_2018c_pivot = df_2018c_pivot.assign(tipo="cabeceras")
    df_2018cp_pivot = df_2018cp_pivot.assign(tipo="centros_poblados_rural_disperso")

    df_2019t_pivot = df_2019t_pivot.assign(tipo="total")
    df_2019c_pivot = df_2019c_pivot.assign(tipo="cabeceras")
    df_2019cp_pivot = df_2019cp_pivot.assign(tipo="centros_poblados_rural_disperso")

    df_2020t_pivot = df_2020t_pivot.assign(tipo="total")
    df_2020c_pivot = df_2020c_pivot.assign(tipo="cabeceras")
    df_2020cp_pivot = df_2020cp_pivot.assign(tipo="centros_poblados_rural_disperso")


    df_2021t_pivot = df_2021t_pivot.assign(tipo="total")
    df_2021c_pivot = df_2021c_pivot.assign(tipo="cabeceras")
    df_2021cp_pivot = df_2021cp_pivot.assign(tipo="centros_poblados_rural_disperso")

#Unión

    df_2018 = pd.concat([df_2018t_pivot, df_2018c_pivot,  df_2018cp_pivot], axis=0)
    df_2019 = pd.concat([df_2019t_pivot, df_2019c_pivot,  df_2019cp_pivot], axis=0)  
    df_2020 = pd.concat([df_2020t_pivot, df_2020c_pivot,  df_2020cp_pivot], axis=0)
    df_2021 = pd.concat([df_2021t_pivot, df_2021c_pivot,  df_2021cp_pivot], axis=0)
    
    
     # Agrega el ano
    df_2018 = df_2018.assign(anio=2018)
    df_2019 = df_2019.assign(anio=2019)
    df_2020= df_2020.assign(anio=2020)
    df_2021= df_2021.assign(anio=2021)

    # Une los dataframes pivote
    df_final = pd.concat([df_2018, df_2019,  df_2020,  df_2021], axis=0)

    # Restablece el índice
    df_final  =df_final .reset_index()
    
    return df_final 


nuevos_nombres = ['departamento','variable', 'total', 'cabeceras', 'centros_poblados_rural_disperso',
                  'total_1', 'cabeceras_1', 'centros_poblados_rural_disperso_1',
                  'total_2', 'cabeceras_2', 'centros_poblados_rural_disperso_2',
                  'total_3', 'cabeceras_3', 'centros_poblados_rural_disperso_3']
nombre_columna = "departamento"

#IPM Variables por departamento
# Ruta al archivo Excel
ruta_archivo = "datos/anexo_dptal_pobreza_multidimensional_21.xls"

# Nombre de la hoja donde están los datos
nombre_hoja = "IPM_Variables_Departamento "


variables_departamento_antioquia = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(14), nrows=15)
variables_departamento_antioquia = procesar_dataframe(variables_departamento_antioquia, nuevos_nombres, nombre_columna)
variables_departamento_antioquia = reordenar_dataframes(variables_departamento_antioquia)


variables_departamento_atlantico = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(40), nrows=15)
variables_departamento_atlantico = procesar_dataframe(variables_departamento_atlantico, nuevos_nombres, nombre_columna)
variables_departamento_atlantico = reordenar_dataframes(variables_departamento_atlantico)


variables_departamento_bogota = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(66), nrows=15)
variables_departamento_bogota = procesar_dataframe(variables_departamento_bogota, nuevos_nombres, nombre_columna)
variables_departamento_bogota = reordenar_dataframes(variables_departamento_bogota)


variables_departamento_bolivar = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(92), nrows=15)
variables_departamento_bolivar = procesar_dataframe(variables_departamento_bolivar, nuevos_nombres, nombre_columna)
variables_departamento_bolivar = reordenar_dataframes(variables_departamento_bolivar)


variables_departamento_boyaca = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(118), nrows=15)
variables_departamento_boyaca = procesar_dataframe(variables_departamento_boyaca, nuevos_nombres, nombre_columna)
variables_departamento_boyaca = reordenar_dataframes(variables_departamento_boyaca)

variables_departamento_caldas = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(144), nrows=15)
variables_departamento_caldas = procesar_dataframe(variables_departamento_caldas, nuevos_nombres, nombre_columna)
variables_departamento_caldas = reordenar_dataframes(variables_departamento_caldas)


variables_departamento_caqueta = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(170), nrows=15)
variables_departamento_caqueta = procesar_dataframe(variables_departamento_caqueta, nuevos_nombres, nombre_columna)
variables_departamento_caqueta = reordenar_dataframes(variables_departamento_caqueta)


variables_departamento_cauca = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(196), nrows=15)
variables_departamento_cauca = procesar_dataframe(variables_departamento_cauca, nuevos_nombres, nombre_columna)
variables_departamento_cauca = reordenar_dataframes(variables_departamento_cauca)

variables_departamento_cesar = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(222), nrows=15)
variables_departamento_cesar = procesar_dataframe(variables_departamento_cesar, nuevos_nombres, nombre_columna)
variables_departamento_cesar = reordenar_dataframes(variables_departamento_cesar)


variables_departamento_cordoba = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(248), nrows=15)
variables_departamento_cordoba = procesar_dataframe(variables_departamento_cordoba, nuevos_nombres, nombre_columna)
variables_departamento_cordoba = reordenar_dataframes(variables_departamento_cordoba)

variables_departamento_cundinamarca = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(274), nrows=15)
variables_departamento_cundinamarca = procesar_dataframe(variables_departamento_cundinamarca, nuevos_nombres, nombre_columna)
variables_departamento_cundinamarca = reordenar_dataframes(variables_departamento_cundinamarca)


variables_departamento_choco = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(300), nrows=15)
variables_departamento_choco = procesar_dataframe(variables_departamento_choco, nuevos_nombres, nombre_columna)
variables_departamento_choco = reordenar_dataframes(variables_departamento_choco)

variables_departamento_huila = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(326), nrows=15)
variables_departamento_huila = procesar_dataframe(variables_departamento_huila, nuevos_nombres, nombre_columna)
variables_departamento_huila = reordenar_dataframes(variables_departamento_huila)


variables_departamento_la_guajira = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(352), nrows=15)
variables_departamento_la_guajira = procesar_dataframe(variables_departamento_la_guajira, nuevos_nombres, nombre_columna)
variables_departamento_la_guajira = reordenar_dataframes(variables_departamento_la_guajira)


variables_departamento_magdalena = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(378), nrows=15)
variables_departamento_magdalena = procesar_dataframe(variables_departamento_magdalena, nuevos_nombres, nombre_columna)
variables_departamento_magdalena = reordenar_dataframes(variables_departamento_magdalena)


variables_departamento_meta = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(404), nrows=15)
variables_departamento_meta = procesar_dataframe(variables_departamento_meta, nuevos_nombres, nombre_columna)
variables_departamento_meta = reordenar_dataframes(variables_departamento_meta)


variables_departamento_narino = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(430), nrows=15)
variables_departamento_narino = procesar_dataframe(variables_departamento_narino, nuevos_nombres, nombre_columna)
variables_departamento_narino = reordenar_dataframes(variables_departamento_narino)


variables_departamento_norte_de_santander = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(456), nrows=15)
variables_departamento_norte_de_santander = procesar_dataframe(variables_departamento_norte_de_santander, nuevos_nombres, nombre_columna)
variables_departamento_norte_de_santander = reordenar_dataframes(variables_departamento_norte_de_santander)


variables_departamento_quindio = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(482), nrows=15)
variables_departamento_quindio = procesar_dataframe(variables_departamento_quindio, nuevos_nombres, nombre_columna)
variables_departamento_quindio = reordenar_dataframes(variables_departamento_quindio)


variables_departamento_risarlda = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(508), nrows=15)
variables_departamento_risarlda = procesar_dataframe(variables_departamento_risarlda, nuevos_nombres, nombre_columna)
variables_departamento_risarlda = reordenar_dataframes(variables_departamento_risarlda)


variables_departamento_santander = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(534), nrows=15)
variables_departamento_santander = procesar_dataframe(variables_departamento_santander, nuevos_nombres, nombre_columna)
variables_departamento_santander = reordenar_dataframes(variables_departamento_santander)


variables_departamento_sucre = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(560), nrows=15)
variables_departamento_sucre = procesar_dataframe(variables_departamento_sucre, nuevos_nombres, nombre_columna)
variables_departamento_sucre = reordenar_dataframes(variables_departamento_sucre)


variables_departamento_tolima = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(586), nrows=15)
variables_departamento_tolima = procesar_dataframe(variables_departamento_tolima, nuevos_nombres, nombre_columna)
variables_departamento_tolima = reordenar_dataframes(variables_departamento_tolima)


variables_departamento_valle_del_cauca = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(612), nrows=15)
variables_departamento_valle_del_cauca = procesar_dataframe(variables_departamento_valle_del_cauca, nuevos_nombres, nombre_columna)
variables_departamento_valle_del_cauca = reordenar_dataframes(variables_departamento_valle_del_cauca)



variables_departamento_arauca = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(638), nrows=15)
variables_departamento_arauca = procesar_dataframe(variables_departamento_arauca, nuevos_nombres, nombre_columna)
variables_departamento_arauca = reordenar_dataframes(variables_departamento_arauca)



variables_departamento_casanare = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(664), nrows=15)
variables_departamento_casanare = procesar_dataframe(variables_departamento_casanare, nuevos_nombres, nombre_columna)
variables_departamento_casanare = reordenar_dataframes(variables_departamento_casanare)


variables_departamento_putumayo = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(690), nrows=15)
variables_departamento_putumayo = procesar_dataframe(variables_departamento_putumayo, nuevos_nombres, nombre_columna)
variables_departamento_putumayo = reordenar_dataframes(variables_departamento_putumayo)



variables_departamento_san_andres = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(716), nrows=15)
variables_departamento_san_andres = procesar_dataframe(variables_departamento_san_andres, nuevos_nombres, nombre_columna)
variables_departamento_san_andres = reordenar_dataframes(variables_departamento_san_andres)


variables_departamento_amazonas = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(742), nrows=15)
variables_departamento_amazonas = procesar_dataframe(variables_departamento_amazonas, nuevos_nombres, nombre_columna)
variables_departamento_amazonas = reordenar_dataframes(variables_departamento_amazonas)


variables_departamento_guainia = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(768), nrows=15)
variables_departamento_guainia = procesar_dataframe(variables_departamento_guainia, nuevos_nombres, nombre_columna)
variables_departamento_guainia = reordenar_dataframes(variables_departamento_guainia)


variables_departamento_guaviare = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(794), nrows=15)
variables_departamento_guaviare = procesar_dataframe(variables_departamento_guaviare, nuevos_nombres, nombre_columna)
variables_departamento_guaviare = reordenar_dataframes(variables_departamento_guaviare)


variables_departamento_vaupes = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(820), nrows=15)
variables_departamento_vaupes = procesar_dataframe(variables_departamento_vaupes, nuevos_nombres, nombre_columna)
variables_departamento_vaupes = reordenar_dataframes(variables_departamento_vaupes)

variables_departamento_vichada = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(846), nrows=15)
variables_departamento_vichada = procesar_dataframe(variables_departamento_vichada, nuevos_nombres, nombre_columna)
variables_departamento_vichada = reordenar_dataframes(variables_departamento_vichada)


variables_departamento = pd.concat([variables_departamento_antioquia, variables_departamento_atlantico,variables_departamento_bogota,
                                    variables_departamento_bolivar,variables_departamento_boyaca,variables_departamento_caldas,
                                    variables_departamento_caqueta,variables_departamento_cauca,variables_departamento_cesar,
                                    variables_departamento_cordoba,variables_departamento_cundinamarca,variables_departamento_choco,
                                    variables_departamento_huila,variables_departamento_la_guajira,variables_departamento_magdalena,
                                    variables_departamento_meta,variables_departamento_narino,variables_departamento_norte_de_santander,
                                    variables_departamento_quindio,variables_departamento_risarlda,variables_departamento_santander,
                                    variables_departamento_sucre,variables_departamento_tolima,variables_departamento_valle_del_cauca,
                                    variables_departamento_arauca,variables_departamento_casanare,variables_departamento_putumayo, 
                                    variables_departamento_san_andres, variables_departamento_amazonas,variables_departamento_guainia,
                                    variables_departamento_guaviare,variables_departamento_vaupes,variables_departamento_vichada], axis=0)



variables_departamento=variables_departamento.reset_index()

# Guardar el DataFrame 
variables_departamento.to_csv('salidas/variables_departamento.csv', index=False)









