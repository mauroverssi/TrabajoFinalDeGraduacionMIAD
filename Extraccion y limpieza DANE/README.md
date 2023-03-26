
En esta carpeta se encuentra el proceso de extracción y limpieza del archivo del DANE con los datos del IPM por región y departamento. 

## Carpetas


- __Datos__: carpeta con los archivos de Excel del DANE
- __Scripts__: carpeta con los scripts en python con el proceso de extracción de los datos. Son 4 archivos: 
	- _Extraer ipm por departamentos_: proceso para extraer los datos de la hoja que tiene el IPM por departamento. 
	- _Extraer ipm por regiones_: proceso para extraer los datos de la hoja que tiene el IPM por regiones.
	- _IPM Variables Departamento_: proceso para extraer los datos de la hoja que tiene el IPM desagregado por tipo de variable y para cada departamento. 
	- _IPM Variables Region_: proceso para extraer los datos de la hoja que tiene el IPM desagregado por tipo de variable y para cada region. 
- __Salidas__: carpetas con los archivos en .csv con los resultados de correr los scripts anteriores, los archivos son: 
	- _departamentos_: lista de departamentos. 
	- _regiones_: lista de regiones. 
	- _ipm_departamentos_final_: dataframe con el ipm por departamento. 
	- _ipm_regiones_final_: dataframe con el ipm por region. 
	- _variables departamento_: ipm desagregado por variables para cada departamento. 
	- _variables region_: ipm desagregado por variables para cada región. 