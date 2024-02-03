# Importar librerías:
import fastparquet                                                  # Lectura y escritura parquet eficiente.
import numpy                                                        # Operaciones numéricas eficientes y arrays.
from fastapi import FastAPI                                         # Desarrollo rápido de APIs
from typing import List                                             # Definición de tipos en Python
import pandas as pd                                                 # Para abrir y editar los archivos 
import ast                                                          # Para expandir listas

#-------------------------------------------------------------------------------------------------------------------------------

app = FastAPI() # Crear Api

# Cargar datos desde el CSV y convertir en df para iniciar la aplicación:

End1_Developer = pd.read_csv('Data/End1_Developer.csv', quotechar='"')                     # Endpoint 1
End2_User = pd.read_parquet('Data/End2_User.parquet')                                      # Endpoint 2
UReviews_F = pd.read_csv('Data/UReviews_F.csv', quotechar='"')                             # Endpoint 2
End3_Genre_User = pd.read_parquet('Data/End3_Genre_User.parquet')                          # Endpoint 3
End4_BestDeveloperYear = pd.read_csv('Data/End4_BestDeveloperYear.csv', quotechar='"')     # Endpoint 4
End5_Sentimiento = pd.read_csv('Data/End5_Sentimiento.csv', quotechar='"')                 # Endpoint 5
similitud_df= pd.read_csv('Data/similitud_df.csv', quotechar='"')                          # Modelo de recomendación ML
names= pd.read_csv('Data/names.csv', quotechar='"')                                        # Modelo de recomendación ML

# Saludo Inicial    -------------------------------------------------------------------------------------------------------
@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi proyecto MLOps/ Luis David Rojas Díaz"}

# Fórmula Endpoint 1  -----------------------------------------------------------------------------------------------------

@app.get("/developerStats/{developer}")
def read_developer_stats(developer: str):

    # Filtrar el DataFrame por desarrollador
    developer_df = End1_Developer[End1_Developer['developer'] == developer]

    # Calcular la cantidad de items y el porcentaje de contenido gratuito por año
    stats_by_year = developer_df.groupby('release_year').agg({'id': 'count', 'price': lambda x: (x == 0).sum() / len(x) * 100}).reset_index()
    stats_by_year.columns = ['release_year', 'item_count', 'free_content_percentage']

    # Convertir los resultados a una lista de diccionarios
    result_list = stats_by_year.to_dict(orient='records')

    return result_list

# Fórmula Endpoint 2  -----------------------------------------------------------------------------------------------------

@app.get("/userData/{user_id}")
 
def userdata(User_id):

    # Filtrar el DataFrame End2_User por user_id
    user_df = End2_User[End2_User['user_id'] == User_id]

    # Calcular la cantidad de dinero gastado por el usuario
    total_money_spent = user_df['price'].sum()

    # Calcular la cantidad de items
    total_items = len(user_df)

    # Filtrar el DataFrame UReviews_F por item_ids relacionados con el usuario
    user_reviews_df = UReviews_F[UReviews_F['user_id'] == User_id]

    # Calcular el porcentaje de recomendación basado en elementos únicos
    unique_items_count = user_reviews_df['item_id'].nunique()
    unique_items_with_recommendation = user_reviews_df[user_reviews_df['recommend'] == True]['item_id'].nunique()
    recommendation_percentage = (unique_items_with_recommendation / unique_items_count) * 100 if unique_items_count > 0 else 0

    # Crear el diccionario de resultados
    result_dict = {
        "Usuario": User_id,
        "Dinero gastado": f"{total_money_spent} USD",
        "% de recomendación": f"{recommendation_percentage:.2f}%",
        "Cantidad de items": total_items
    }

    return result_dict

# Fórmula Endpoint 3  -----------------------------------------------------------------------------------------------------

@app.get("/userForGenre/{genero}")

def UserForGenre(genero: str):
    # Filtrar UserForGenre por el género dado
    genre_data = End3_Genre_User[End3_Genre_User['genres'] == genero]

    # Encontrar al usuario con más horas jugadas para el género dado
    max_hours_user = genre_data.loc[genre_data['playtime_forever_x'].idxmax()]['user_id']

    # Crear una lista de la acumulación de horas jugadas por año de lanzamiento
    hours_by_year = genre_data.groupby('release_year')['playtime_forever_y'].sum().reset_index()
    hours_by_year_list = [{"Año": int(year), "Horas": int(hours)} for year, hours in hours_by_year.values]

    # Crear el diccionario de resultados
    result_dict = {
        f"Usuario con más horas jugadas para el género {genero}": max_hours_user,
        "Horas jugadas": hours_by_year_list
    }

    return result_dict

# Fórmula Endpoint 4  -----------------------------------------------------------------------------------------------------

@app.get("/userDeveloperYear/{year}")

def best_developer_year(year: int):
  
    # Filtrar End4_BestDeveloperYear por el año dado
    filtered_data = End4_BestDeveloperYear[End4_BestDeveloperYear['posted_year'] == year]

    # Filtrar por juegos más recomendados (recommend = Verdadero y comentarios positivos)
    top_developers = filtered_data[filtered_data['count'] > 0]

    # Sumar los conteos por desarrollador y obtener el ranking de los 3 mejores desarrolladores
    top3_developers = top_developers.groupby('developer')['count'].sum().nlargest(3).reset_index()

    # Crear un diccionario de resultados
    result_dict = {"Puesto {}".format(i + 1): developer for i, developer in enumerate(top3_developers['developer'])}

    return result_dict

# Fórmula Endpoint 5  -----------------------------------------------------------------------------------------------------

@app.get("/analysis/{ReviewsDeveloper}")

def desarrollador_reviews_analysis(ReviewsDeveloper: str):
   
    # Filtrar End5_Sentimiento por el desarrollador dado
    desarrollador_data = End5_Sentimiento[End5_Sentimiento['developer'] == ReviewsDeveloper]

    # Verificar si el desarrollador existe en el DataFrame
    if not desarrollador_data.empty:
        # Obtener la cantidad de reseñas positivas y negativas
        negative_count = int(desarrollador_data['Negative'])
        positive_count = int(desarrollador_data['Positive'])

        # Crear el diccionario de resultados
        result_dict = {ReviewsDeveloper: {'Negative': negative_count, 'Positive': positive_count}}

        return result_dict
    else:
        return {ReviewsDeveloper: {'Negative': 0, 'Positive': 0}}

# Modelo ML Recomendación de Videojuegos ------------------------------------------------------------------------------------

@app.get("/recommended_games/{id_seleccionado}")

def obtener_nombres_recomendados(id_seleccionado:int):
    # Obtener el nombre del juego seleccionado
    nombre_seleccionado = names.loc[names['id'] == id_seleccionado, 'app_name'].iloc[0]

    # Obtener los IDs de los juegos recomendados
    juegos_recomendados_ids_str = similitud_df.loc[similitud_df['id'] == id_seleccionado, 'recommended_id'].iloc[0]

    # Convertir la cadena a una lista de números
    juegos_recomendados_ids = ast.literal_eval(juegos_recomendados_ids_str)

    # Obtener los nombres de los juegos recomendados
    nombres_recomendados = []
    for id_recomendado in juegos_recomendados_ids:
        # Verificar si id_recomendado es un número antes de intentar obtener el nombre
        if isinstance(id_recomendado, (int, float)):
            # Obtener el nombre del juego recomendado
            nombre_recomendado = names.loc[names['id'] == id_recomendado, 'app_name'].iloc[0]
            nombres_recomendados.append(nombre_recomendado)

    # Crear y devolver el diccionario
    diccionario_resultado = {'nombre_seleccionado': nombre_seleccionado, 'nombres_recomendados': nombres_recomendados}
    return diccionario_resultado

