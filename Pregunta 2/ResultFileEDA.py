import pandas as pd

#Cargar los archivos CSV de propiedades y reservas
prop = pd.read_csv('1728311703514.csv')
reserv = pd.read_csv('1728311703515.csv')

#Combinamos los Datraframes creados a tráves del ID en ambos archivos
result = pd.merge(prop,reserv, on='PropertyId', how='inner')

#Ordamos el consolidado por el Id de la propiedad
result = result.sort_values(by='PropertyId')

#Guardamos el resultado obtenido en un nuevo archivo CSV
result.to_csv('ResultFileEDA.csv', index=False)