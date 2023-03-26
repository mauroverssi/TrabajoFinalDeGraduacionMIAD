# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:51:33 2023

@author: PC
"""
import pandas as pd


#IPM Regiones
# Ruta al archivo Excel
ruta_archivo = "datos/anexo_dptal_pobreza_multidimensional_21.xls"

# Nombre de la hoja donde están los datos
nombre_hoja = "IPM_Regiones"

# Saltar las primeras 15 filas y leer las filas 16 a 24
ipm_regiones = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja, skiprows=range(14), nrows=9)



nuevos_nombres = ['region', 'total', 'cabeceras', 'centros_poblados_rural_disperso',
                  'total_1', 'cabeceras_1', 'centros_poblados_rural_disperso_1',
                  'total_2', 'cabeceras_2', 'centros_poblados_rural_disperso_2',
                  'total_3', 'cabeceras_3', 'centros_poblados_rural_disperso_3']



# Asignar los nuevos nombres de las columnas al DataFrame
ipm_regiones.columns = nuevos_nombres


ipm_regiones_2018 = ipm_regiones.iloc[:, :4]
ipm_regiones_2019 = ipm_regiones.iloc[:, [0, 4, 5, 6]]
ipm_regiones_2020 = ipm_regiones.iloc[:, [0, 7, 8, 9]]
ipm_regiones_2021 = ipm_regiones.iloc[:, [0, 10, 11, 12]]


#Nuevos nombres 

nuevos_nombres_2 = ['region', 'total', 'cabeceras', 'centros_poblados_rural_disperso']

ipm_regiones_2019.columns = nuevos_nombres_2
ipm_regiones_2020.columns = nuevos_nombres_2
ipm_regiones_2021.columns = nuevos_nombres_2


ipm_regiones_2018 = ipm_regiones_2018.assign(anio=2018)
# Asignar el año 2019 al DataFrame ipm_regiones_2019
ipm_regiones_2019 = ipm_regiones_2019.assign(anio=2019)

# Asignar el año 2020 al DataFrame ipm_regiones_2020
ipm_regiones_2020 = ipm_regiones_2020.assign(anio=2020)

ipm_regiones_2021 = ipm_regiones_2021.assign(anio=2021)


ipm_regiones_final = pd.concat([ipm_regiones_2018, ipm_regiones_2019, ipm_regiones_2020, ipm_regiones_2021], axis=0)


# Resetear el índice del DataFrame
ipm_regiones_final = ipm_regiones_final.reset_index(drop=True)

#Extraer regiones
regiones_unicas = ipm_regiones_final["region"].unique()
regiones = pd.DataFrame(regiones_unicas, columns=["region"])

regiones.to_csv('salidas/regiones.csv', index=False)


# Guardar el DataFrame ipm_regiones_final como un archivo CSV
ipm_regiones_final.to_csv('salidas/ipm_regiones_final.csv', index=False)
























