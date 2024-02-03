# <p align="center"> Proyecto Individual No. 1
# <p align="center"> Machine Learning Operations (MLOps)</p>
<p align="center"> Realizado por:</p>

<p align="center"> Luis David Rojas Díaz</p>
<p align="center"> Estudiante</p>
<p align="center">
  <img src="src/Imagen1.png">
</p>

## Descripción del Proyecto

El Proyecto Individual No. 1, centrado en Machine Learning Operations (MLOps), ha sido concebido con el propósito de analizar y poner en funcionamiento un sistema de recomendación de videojuegos basado en datos de la plataforma Steam. En calidad de Data Scientist, se recibieron tres conjuntos de datos esenciales para la construcción del modelo: información sobre los videojuegos en steam, perfiles de usuarios asociados a cada videojuego, y las recomendaciones específicas realizadas por los usuarios para cada juego. También se pide generar 5 funciones (endpoints) basadas en los datos para ser consumida por FastApi y deployada a través de Render.

![Logo de Proyecto](https://i.pinimg.com/originals/af/8a/9b/af8a9bc9b016a6252b9a3e7e6a6b206e.jpg)


### Datos del proyecto (originales y generado)

| Carpeta        | Tipo      | Nombre              | Formato | Descripción                                       |
|----------------|-----------|---------------------|---------|---------------------------------------------------|
| Original_Data  | Documento | output_steam_games  | json    | Archivo original de videojuegos                   |
| Original_Data  | Documento | australian_user_items | json  | Archivo original de video juegos por usuario      |
| Original_Data  | Documento | australian_user_reviews | json | Archivo original de Comentarios de usuarios por videojuego |
| Revised_Data   | Documento | Steam_Games         | csv     | Archivo revisado de output_steam_games.json       |
| Revised_Data   | Documento | User_Items          | csv     | Archivo revisado de australian_user_items.json    |
| Revised_Data   | Documento | User_Reviews        | csv     | Archivo revisado de australian_user_reviews.json  |
| Clean_Data     | Documento | Genres_Items        | csv     | Originado del ETL de Steam_Games.csv               |
| Clean_Data     | Documento | SGames_CD           | csv     | Originado del ETL de Steam_Games.csv               |
| Clean_Data     | Documento | UItems_CD           | csv     | Originado del ETL de User_Items.csv                |
| Clean_Data     | Documento | UReviews_CD         | csv     | Originado del ETL de User_Reviews.csv             |
| Data_Queries   | Documento | End1_Developer      | csv     | Generado de SGames_CD.csv para el Endpoint 1      |
| Data_Queries   | Documento | End2_User           | paquet  | Generado de UItems_CD.csv para el Endpoint 2      |
| Data_Queries   | Documento | UReviews_F          | csv     | Generado de UReviws_CD.csv Endpoint 2              |
| Data_Queries   | Documento | End3_Genre_User     | paquet  | Generado de SGames_CD.csv y Genres_items.csv para el Endpoint 3 |
| Data_Queries   | Documento | End4_BestDeveloperYear | csv | Generado de UReviews_CD.csv para el Endpoint 4    |
| Data_Queries   | Documento | End5_Sentimiento    | csv     | Generado de UReviews_CD.csv y SGames_CD.csv para el Endpoint 5 |
| Data_Queries   | Documento | names               | csv     | Generado de SGames_CD.csv para el Modelo de Recomendación |
| Data_Queries   | Documento | similitud           | csv     | Creado a partir del modelo de similitud de coseno  |
| --             | Documento | Diccionario de Datos STEAM | txt | Diccionario de los datos originales "Original_Data" |
| --             | Documento | 1. EDA_Datos_Originales | ipynb | Notebook del EDA preliminar                        |
| --             | Documento | 2. ETL              | ipynb   | ETL de los archivos revisados en "Revised_Data"    |
| --             | Documento | 3. EDA_Datos_Limpios | ipynb   | EDA sobre los datos en "Clean_Data"                |
| --             | Documento | 4. Funciones_Endpoints | ipynb | Notebook sobre las funciones de los endpoints      |
| --             | Documento | 5. Modelo_Recomendación | ipynb | Notebook para el modelo de recomendación            |
| --             | Documento | main                | py      | Scripts para FastApi                               |
| --             | Documento | requirements        | txt     | Lista de aplicaciones necesarias para las descargas de librerías en Render |


Debido a la capacidad sobre el tamaño de los archivos que permite GitHub solo se dejan en este proyecto los datos de la carpeta "Data_Queries" que son los ncesarios para los endpoints y el modelo de recomendación. También se dejan todos los notebooks, el scrip para la FastApi (main.py) y los requerimientos de librerías para Render (requirements.txt). Los demás archivos están disponibles en el sigueinte link:

Dirección de archivos:
https://drive.google.com/drive/u/0/folders/16DS0VBpu_QNGv1l6Mf9Q0RqZMTWgZpo_

## Desarrollo del Proyecto

### 1. Análisis Exploratorio de Datos (EDA) Preliminar

La primera fase consistió en un EDA preliminar donde se examinaron los archivos para comprender su estructura, eliminar registros nulos y esbozar transformaciones necesarias. Este paso sienta las bases para las siguientes etapas del proyecto.

Se tomaron los archivos guardados en la carpeta "Original_Data", se creó un dataframe por cada archivo con los datos limpios y se guardó en la carpeta "Revised_Data".

[ver notebook "1. EDA_Datos_Originales.ipynb"](1.%20EDA_Datos_Originales.ipynb)

### 2. Transformación de Datos

Basándonos en el EDA preliminar, se llevaron a cabo transformaciones de los datos, incluyendo la eliminación de nulos e imputación de valores. Se tomó la decisión de no desanidar datos anidados en el archivo de video juegos (Steam_games.csv), porque se consideró necesario para el modelo de recomendación. Esto más adelante se realizó para las funciones, por lo que en el proceso de ETL se guardó el archivo auxiliar que guarda el id de cada juego y el genero desanidado (expandido).

Se tomaron los archivos guardados en la carpeta "Revised_Data"., se creó un dataframe por cada uno, luego haber limpiado e imputado los datos, para luego guardarlos en la carapeta "Clean_Data".

[ver notebook "2. ETL.ipynb"](2.%20ETL.ipynb)

### 3. EDA de Datos Limpios

Con los datos transformados, se realizó un EDA exhaustivo para analizar estadísticas sobre los juegos más jugados, géneros predominantes, años con más lanzamientos y relaciones entre las tres bases de datos.

En este EDA al contener datos expandidos, se analiza la estructura de los datos en función de la creación de los endpoints y el modelo de recomendación; se documentan las limpiezas posteriores o arreglos que deberías hacerse en la etapa posterior en la creación de las funciones y el modelo de recomendación.

[ver notebook "3. EDA_Datos_Limpios.ipynb"](3.%20EDA_Datos_Limpios.ipynb)


### 4. Funciones para Endpoints de la API

Se desarrollaron funciones para los endpoints de la aplicación FastAPI utilizando consultas específicas para garantizar la eficiencia y optimización del tamaño de los archivos en GitHub. Se llevaron a cabo pruebas de ensayo y error para superar las limitaciones de tamaño de archivos en GitHub.

[para ver el desarrrollo en la creación de funciones ver el notebook "4. Funciones_Endpoints.ipynb"](4.%20Funciones_Endpoints.ipynb)

Descipción de funciones:

### 4.1. Función de Registro por Desarrollador

def developer_stats( developer : str ): recibe el nombre de un desarrollador y devuelve la cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

Ejemplo de retorno:
| Año  | Cantidad de artículos | Contenido Gratis |
|------|------------------------|-------------------|
| 2023 | 50                     | 27%               |
| 2022 | 45                     | 25%               |
| xxxx | xx                     | x%                |


### 4.2. Función de datos de usuario

def userdata(User_id: int): Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.

Ejemplo de retorno: {"Usuario X" : us213ndjss09sdf, "Dinero gastado": 200 USD, "% de recomendación": 20%, "cantidad de items": 5}

### 4.3. Función de mejor usuario por género de video juego

def UserForGenre(genero: str): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas : 23}]}

### 4.4. Función de top 3 mejores desarrolladores por año

def best_developer_year(año: int): Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = Verdadero y comentarios positivos)

Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

### 4.5. Función percepción por desarrollador

def desarrollador_reviews_analysis(ReviewsDeveloper: str): Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentran categorizados con un análisis de sentimiento como valor positivo o negativo.

Ejemplo de retorno: {'Valve' : [Negative = 182, Positive = 278]}

### 5. Creación del Modelo de Recomendación

Se creó un modelo de recomendación basado en similitud de coseno, utilizando una matriz de coseno sobre los datos del archivo SGames_CD.csv. El modelo identifica para un "id" (video juego) seleccionado los "ids" (video juegos") que más se parecen (se limita a un top 5 de los más parecidos). A continuación los paso para el desarrollo del modelo:

- Eliminación de registros nulos en las columnas relevantes para el modelo.
- Transformación de la columna "genre" y "specs" en cadena para facilitar la lectura de modelo (quital la lista de datos anidados).
- Eliminación de comillas, corchetes, comas y reemplazar guiones por espacios en las columnas "genre" y "specs".
- Toquenización y normalización de las columnas "genre" y "specs".
- Codificación (one-Hot Encoded) de "publisher" y "developer".
- Vectorización de las columnas en una matrix de recuentos.
- Cálculo de la similitud de coseno (creción de matrix).

Al obtener la matrix de similitud de coseno, se creó un nuevo datafrome donde se tenía la lista de lo videojuegos y sobre esta se iteró el modelo para obtener por cada item en una columna la lista de los "ids" más parecidos que serían los recomendados según el ítem específico. El archivo se guardó en la carpeta "data_Queries" con el nombre de "similitud". Se guardó otro archivo auxiliar con el "id" y nombres de video juegos, para crear una fórmula. 

La fórmula es def obtener_nombres_recomendados(id_seleccionado:int). Esta recibe como entrada un "id" de video juego para obtener como resultado la lista de los 5 que se recomiendan según este "id".

ejemplo de salida:

{'juego_seleccionado': 'Real Pool 3D - Poolians',
    'juegos_recomendados': 
        ['Fantasy Grounds - Mini-Dungeon #023: The Aura of Profit (5E)',
        'One Hit KO',
        'Hack_me 2 - Wallpapers',
        'Trimmer Tycoon',
        'Rocksmith® 2014 – 2010s Mix Song Pack']}

[ver el desarrollo del modelo en el notebook "5. Modelo_Recomendación.ipynb"](5.%20Modelo_recomendación.ipynb)

### 6. Implementación de FastAPI y Despliegue en Render

Se crearon archivos de FastAPI, se realizaron pruebas locales en un entorno virtual y finalmente se desplegó el modelo a través de Render, permitiendo el acceso a través de la web.

Las funciones creadas para los endpoints de FastApi y el modelo de recomendación se transformó a las estructura necesaria para la lectura de la aplicación durante el entorno virtual de manera local. Se realizaron pruebas hasta garantizar que todas las funciones corrían en FastApi para proceder al despliegue en Render.

En Render se realizan decenas de pruebas corrigiendo escritura de algunas funciones y sobre todo en las direcciones de los archivos para lograr que finamente funcionara la aplicación en la web.

Para el desarrollo se siguieron los pasos del tutorial en el siguiente link: [tutorial FastApi y Render](https://github.com/HX-FNegrete/render-fastapi-tutorial)

Los pasos resumidos son:

- Creación un entorno virtual (para probar FastApi)
- Creación un script llamado main.py donde se consignan todas las funciones e importaciones de librerías necesarias para la ejecución de las fórmulas, incluyendo la aplicación FastApi. [Ver archivo main.py](main.py)
- Creación la lista de requerimientos de librerías necesarias para correr las funciones. [Ver archivo requirements.txt](requirements.txt)
- Creación de un repositorio público en GitHub (este repositorio).
- Sincronización del repositorio local al repositorio de GitHub.
- Creación de una cuenta en Render (render.com).
- Conexión del servicio al repositorio en GitHub.
- Creación de servicio web en Render.
- Ingreso al enlace para consumir la Api en la web.

### 7. Video explicando el funcionamiento de FastApi deployado con Render

A continuación se relaciona el link que corresponde a un video que explica el funcionamiento de la Api deployada mostrando el uso de cada uno de los endpoints directamente en servicio web:



# Despedida

¡Gracias por visitar mi proyecto! Epero que sea útil esta documentación y sea comprensible el código. Cualquier pregunta, problema o sugerencia, por favor contactarte conmigo. ¡Agradezco su interés y apoyo!

Happy coding! 🚀

Att,

Luis David Rojas Díaz