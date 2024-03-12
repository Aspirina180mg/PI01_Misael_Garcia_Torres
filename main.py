# librerias utilizadas

import zipfile
import gzip
import json
import ast
import nlt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


# Creación de API
app = FastAPI()

# lectura de los datos
df_funcion1 = 
df_funcion2 = 
df_funcion3 = 
df_funcion4 = 
df_funcion5 = 

#Endpoints de la API
#@profile
@app.get('/playtime_genre/{genre}')
async def PlayTimeGenre(genre: str):
    '''
    Debe devolver año con mas horas jugadas para dicho género.
    '''
    # Implementa la lógica para obtener el año con más horas jugadas para el género dado
    # Ejemplo: year_with_most_playtime = obtener_año_con_mas_horas_jugadas_para_genero(genre)
    # return {"Año con más horas jugadas para el género": year_with_most_playtime}
    pass

@app.get('/user_for_genre/{genre}')
async def UserForGenre(genre: str):
    '''
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
    '''
    # Implementa la lógica para obtener el usuario con más horas jugadas para el género dado y la acumulación de horas jugadas por año
    # Ejemplo de retorno: {"Usuario con más horas jugadas para Género X": user_with_most_playtime, "Horas jugadas": horas_por_año}
    pass

@app.get('/users_recommend/{year}')
async def UsersRecommend(year: int):
    '''
    Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
    '''
    # Implementa la lógica para obtener el top 3 de juegos más recomendados para el año dado
    # Ejemplo de retorno: [{"Puesto 1": juego_1}, {"Puesto 2": juego_2}, {"Puesto 3": juego_3}]
    pass

@app.get('/users_not_recommend/{year}')
async def UsersNotRecommend(year: int):
    '''
    Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
    '''
    # Implementa la lógica para obtener el top 3 de juegos menos recomendados para el año dado
    # Ejemplo de retorno: [{"Puesto 1": juego_1}, {"Puesto 2": juego_2}, {"Puesto 3": juego_3}]
    pass

@app.get('/sentiment_analysis/{year}')
async def SentimentAnalysis(year: int):
    '''
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
    '''
    # Implementa la lógica para obtener la cantidad de registros de reseñas con análisis de sentimiento para el año dado
    # Ejemplo de retorno: {"Año": year, "Cantidad de registros con análisis de sentimiento": cantidad_registros_sentimiento}
    pass