# <h1 align=center>**`Proyecto: Machine Learning Operations (MLOps)`**</h1>

_El presente proyecto consiste en la creación un modelo de recomendación de peliculas utilizando técnicas de machine learning. Para este proposito se realizo un proceso secuencial de ETL(Extract, Transform y Load), EDA(Exploratory Data Analysis), modelamiento y finalmente el deployment._
_A continuación se brinda una guia y descripción de los procesos mencionados._

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

_Para instalar las dependencias necesarias puedes ejecutar el siguiente codigo en tu consola de comandos una vez tengas el repositorio localmente:_
```
pip install -r requirements.txt
```

### Instalación 🔧

1. Clona este repositorio con Git o manualmente.
2. Instala Python y las dependencias necesarias definidas en el archivo requirements.txt
3. El IDE con el cual se desarrollo el proyecto fue Visual Studio Code, se recomienda el mismo.
4. Ejecuta el archivo main.py para ver el proyecto en funcionamiento localmente.

Por ultimo, mira **Deployment** para conocer como desplegar el proyecto y para acceder al link del proyecto.



## Construcción del proyecto ⚙️

_En esta parte se detalla como esta fue elaborado el proyecto y como se encuentra estructurado_

### ETL (Extract, Transform and Load) :wrench:

_El proceso ETL consistió en la limpieza y mejora de una base de datos de peliculas que se encuentran el archivo comprimido [`Datasets.rar`](https://github.com/MBernal6/MLOps-Proyecto01/blob/main/Datasets.rar) con el fin de que pueda ser utilizada en el modelamiento._
_La totalidad del proceso se encuentra en el notebook [`ETL.ipynb`](https://github.com/MBernal6/MLOps-Proyecto01/blob/main/ETL.ipynb) a continuación se detalla las transformaciones principales para lograr el MVP(Producto Mínmo Viable:)_

1. Selección y carga del dataset: La exploración inicial de los datasets se realizó en el notebook [`Borrador.ipynb`](https://github.com/MBernal6/MLOps-Proyecto01/blob/main/Borrador.ipynb), una vez seleccionado se procedio a su transformación.
2. Las transformaciones realizadas fueron las siguientes:
+ Eliminación de las columnas: video,imdb_id,adult,original_title,poster_path y homepage.
+ Cambio de los valores nulos de las columnas Revenue y Budget por el valor 0.
+ Eliminación de los valores nulos del campo Release Date.
+ Cambio de formato del campo Release Date a AAAA-mm-dd y extracción del año en una nueva columna.
+ Creación de la columna Return.
+ Desanidación de los valores de tipo diccionario.
+ Extracción del nombre del director del dataset credits.csv
+ Unión de los datasets y eliminación de columnas anidadas.
3. Por último, con el dataframe trabajado se generó un nuevo archivo `movies_final.csv` para ser explorado a profundidad y servir como input para el modelo de recomendación de peliculas.
    
### EDA (Exploratory Data Analysis) :mag_right:

_Antes del modelamiento es necesario entender los datos obtenidos, con dicho fin se realizo un proceso de exploración.  El objetivo principal de este análisis es identificar patrones, tendencias y variables relevantes que servirán como base para la construcción de un modelo preciso de Machine Learning, destinado a la recomendación de películas. A través del EDA, buscaremos comprender en profundidad la naturaleza de los datos, detectar posibles relaciones entre variables clave y descubrir características significativas._
_Los principales puntos desarrollados se encuentran en el notebook [`EDA.ipynb`](https://github.com/MBernal6/MLOps-Proyecto01/blob/main/EDA.ipynb), los cuales se resumen de la siguiente manera:_

1. `Exploración inicial del dataset`: Donde se determinó que columnas o variables deberían tener una análisis más profundo, se conocio a detalle el tipo de datos y la cantidad de valores nulos.
2. `Análisis univariable`: Se exploraron las variables 'title', 'géneros', 'collection', 'overview', 'año de lanzamiento' y un resumen estadistico de las variables númericas.
<p align="center">
  <img src= "https://github.com/MBernal6/MLOps-Proyecto01/assets/115516183/939f8759-f09f-4b37-a084-454705e1ea51") height=300>
</p>

3. `Análisis bivariado y multivariable`: Se realizó una matriz de correlaciones y gráficos de dispersión para determinar el comportamiento de las variables númericas.

_Como conclusión del EDA se decidieron tomar las variables title, género, overview y promedio de puntaje para crear el modelo de recomendaciones._

### Modelamiento ⌨️

_El modelo de recomendación utilizó el algoritmo de similitud de cosenos para determinar la medida de similitud de las variables y de este ponderar las 5 principales recomendaciones._
_La idea original era considerar el promedio de votos de cada pelicula para calcular la similitud de coseno, sin embargo el procesamiento requeria mayores recursos, siendo especificos una mayor cantidad de memoria RAM disponible._
_Es por ello que el modelo final contemplo las siguientes variables: Title, género y corporaciones._
_El desarrollo completo se encuentra detallado en [`Modelo_Recomendacion.ipynb`](https://github.com/MBernal6/MLOps-Proyecto01/blob/main/Modelo_Recomendacion.ipynb)_

## Deployment 📦
### Desarrollo de API
_La API fue desarrollado con FastAPI, y contiene los siguientes funcionalidades:_
1. Búsqueda de peliculas por idioma.
2. Duración y año de lanzamiento de cada pelicula.
3. Búsqueda de peliculas por franquicia.
4. Retorno de peliculas producidas en un determinado pais.
5. Búsqueda de productoras exitosas.
6. Búsqueda de directores existosos y peliculas realizadas.
7. Recomendación de 5 peliculas por pelicula solicitada.

### Despliegue
_Para el deployment del proyecto se utilizó [Render](https://render.com/) y para ello se generó localmente el archivo con las dependencias necesarias [`requirements.txt`](https://github.com/MBernal6/MLOps-Proyecto01/blob/main/requirements.txt)_
1. Render se conectó a este repositorio de github y permite visualizar el proyecto en el siguiente link: [MLOps-Mauricio Bernal](https://mlops-mbp.onrender.com/docs)

## Construido con 🛠️

_Las herramientas para la creación del proyecto fueron las siguientes:_

* [Visual Studio Code](https://code.visualstudio.com/) - IDE.
* [Python](https://www.python.org/) - Lenguaje de programación.
* [Pandas](https://pandas.pydata.org/) - Libreria para análisis de datos.
* [Scikit-Learn](https://scikit-learn.org/stable/) - Libreria de Machine Learning. 
* [FastAPI](https://fastapi.tiangolo.com/) -  Marco web moderno para crear API RESTful en Python.
* [Render](https://render.com/) - Servicio de nube para creación y despliegue de aplicaciones.


## Autor ✒️

* **Mauricio Bernal** - *Proyecto Individual N°01-Labs HENRY* - [MBernal6](https://github.com/MBernal6)

## Expresiones de Gratitud 🎁

* Agradecimientos al bootcamp [HENRY](https://www.soyhenry.com/). 
---
⌨️ por [MBernal6](https://github.com/MBernal6) 