# Importamos las librerías
import pandas as pd 
import numpy as np
from fastapi import FastAPI

#Creamoos el objeto "app" que instancia la clase FastAPI y añadimos titulo y descripción
app = FastAPI(title='Proyecto N°01: Machine Learning Operations (MLOps)',
              description='Elaborado por: Mauricio Bernal DSPT-02')

#Definimos los datasets
df = pd.read_csv('movies_final.csv')
df_modelo = pd.read_csv('recomendaciones.csv')

#FUNCIONES

#1. Peliculas en un determinado idioma

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma:str):
    '''Ingresas el idioma, retornando la cantidad de peliculas producidas en el mismo'''
    # Mascara para obtener solo las filas con el idioma proporcionado
    peliculas_en_idioma = df[df['original_language'] == idioma]
    
    # Contar el número de filas resultantes, que corresponde a la cantidad de películas en ese idioma
    respuesta = peliculas_en_idioma.shape[0]

    return {'idioma':idioma, 'cantidad':respuesta}


#2. Duración y año de estreno de una pelicula 
    
@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    '''Ingresas la pelicula, retornando la duracion y el año'''
    #Mascara para obtener la fila de la pelicula buscada
    pelicula_buscada = df[df['title'] == pelicula]

    #Extraemos los valores de las columnas necesaria
    duracion = pelicula_buscada['runtime'].values[0]
    anio = pelicula_buscada['release_year'].values[0]

    return {'pelicula':pelicula, 'duracion':duracion, 'anio':anio}


#3. Peliculas por franquicia 

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    #Mascara para seleccionar las peliculas de una misma franquicia 
    peliculas_franquicia = df[df['collection'] == franquicia]

    #Se calcula la cantidad de peliculas
    cantidad = peliculas_franquicia.shape[0]

    #Se calcula la ganancia total, que se considera como el Revenue que esta definida como:
    ##revenue: 'Recaudación total de la pelicula '
    ganancia_total = peliculas_franquicia['revenue'].sum()

    #Se calcula el promedio usando la columna revenue
    ganancia_promedio = peliculas_franquicia['revenue'].mean()

    return {'franquicia':franquicia, 'cantidad':cantidad, 'ganancia_total':ganancia_total, 'ganancia_promedio':ganancia_promedio}


#4. Peliculas por país

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    # Utilizar 'str.contains()' para verificar en qué filas se encuentra el país proporcionado
    peliculas_en_pais = df[df['production_countrie'].str.contains(pais)]
    
    # Contar el número de filas resultantes, que corresponde a la cantidad de películas en ese país
    cantidad_peliculas = peliculas_en_pais.shape[0]
    
    # Crear y retornar un diccionario con la información solicitada
    return {'pais': pais, 'cantidad': cantidad_peliculas}


#5. Productoras

@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora:str):
    '''Ingresas la productora, entregandote el revunue total y la cantidad de peliculas que realizo '''
    # Utilizar 'str.contains()' para verificar en qué filas se encuentra el país proporcionado
    peliculas_productora = df[df['companies'].str.contains(productora)]
    
    # Sumamos la columna revenue de los datos filtrados 
    revenue_total = peliculas_productora['revenue'].sum()

    # Contar el número de filas resultantes, que corresponde a la cantidad de películas en ese país
    cantidad_peliculas = peliculas_productora.shape[0]

    return {'productora':productora, 'revenue_total': revenue_total,'cantidad':cantidad_peliculas}


#6. Peliculas por director

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. En formato lista'''
    #Mascara para seleccionar las peliculas de un mismo director 
    peliculas_director = df[df['director_name'] == nombre_director]
    if peliculas_director.empty:
        return f'No se encontraron películas del director {nombre_director}.'

    #Calcular el éxito total del director sumando el retorno de todas sus películas
    retorno = peliculas_director['return'].sum()

    # Obtener información detallada de cada película
    peliculas_info = []
    for index, row in peliculas_director.iterrows():
        pelicula_info = {
            'titulo': row['title'],
            'anio': row['release_year'],
            'retorno': row['return'],
            'costo': row['budget'],
            'ganancia': row['revenue']
        }
        peliculas_info.append(pelicula_info)
    
    # Crear y retornar un diccionario con la información solicitada
    return {
        'director': nombre_director,
        'retorno_total_director': retorno,
        'peliculas': peliculas_info
        }


#MODELO DE RECOMENDACIÓN - ML

#La siguiente función accede a un dataset creado a partir del modelo de similitud de coseno

@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    #Creamos mascara para buscar la pelicula 
    recomendaciones = df_modelo[df_modelo['Pelicula'] == titulo]['Recomendaciones'].values[0]
    return {'lista recomendada': recomendaciones}