# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 21:20:10 2023

@author: PC
"""

import pandas as pd


#IPM Regiones
# Ruta al archivo Excel
ruta_archivo = "datos/anexo_dptal_pobreza_multidimensional_21.xls"

# Nombre de la hoja donde están los datos
nombre_hoja = "IPM_Departamentos"

# Saltar las primeras 15 filas y leer las filas 16 a 24
ipm_departamentos = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(14), nrows=33)


nuevos_nombres = ['region', 'total', 'cabeceras', 'centros_poblados_rural_disperso',
                  'total_1', 'cabeceras_1', 'centros_poblados_rural_disperso_1',
                  'total_2', 'cabeceras_2', 'centros_poblados_rural_disperso_2',
                  'total_3', 'cabeceras_3', 'centros_poblados_rural_disperso_3']



# Asignar los nuevos nombres de las columnas al DataFrame
ipm_departamentos.columns = nuevos_nombres


ipm_departamentos_2018 = ipm_departamentos.iloc[:, :4]
ipm_departamentos_2019 = ipm_departamentos.iloc[:, [0, 4, 5, 6]]
ipm_departamentos_2020 = ipm_departamentos.iloc[:, [0, 7, 8, 9]]
ipm_departamentos_2021 = ipm_departamentos.iloc[:, [0, 10, 11, 12]]


#Nuevos nombres 

nuevos_nombres_2 = ['region', 'total', 'cabeceras', 'centros_poblados_rural_disperso']

ipm_departamentos_2019.columns = nuevos_nombres_2
ipm_departamentos_2020.columns = nuevos_nombres_2
ipm_departamentos_2021.columns = nuevos_nombres_2


ipm_departamentos_2018 = ipm_departamentos_2018.assign(anio=2018)
# Asignar el año 2019 al DataFrame ipm_departamentos_2019
ipm_departamentos_2019 = ipm_departamentos_2019.assign(anio=2019)

# Asignar el año 2020 al DataFrame ipm_departamentos_2020
ipm_departamentos_2020 = ipm_departamentos_2020.assign(anio=2020)

ipm_departamentos_2021 = ipm_departamentos_2021.assign(anio=2021)


ipm_departamentos_final = pd.concat([ipm_departamentos_2018, ipm_departamentos_2019, ipm_departamentos_2020, ipm_departamentos_2021], axis=0)


# Resetear el índice del DataFrame
ipm_departamentos_final = ipm_departamentos_final.reset_index(drop=True)

#Extraer departamentos
departamentos_unicos = ipm_departamentos_final["region"].unique()
departamentos = pd.DataFrame(departamentos_unicos, columns=["region"])

departamentos.to_csv('salidas/departamentos.csv', index=False)

# Guardar el DataFrame ipm_departamentos_final como un archivo CSV
ipm_departamentos_final.to_csv('salidas/ipm_departamentos_final.csv', index=False)
