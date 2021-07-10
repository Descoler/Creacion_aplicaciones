# get: leer datos
# post: insertar datos
# put: actualizar datos
# delete: eliminar datos


from fastapi import FastAPI
import pandas as pd # pandas para lectura en formato dataframe
import json # json para transformarlo en formato json
import csv # csv para insertar los datos en él
import os # para reconocer el entorno y usarlo como consola
# donde creamos nuestro modelo de datos
from pydantic import BaseModel

# creamos la primera aplicación fastAPI llamada “app”:
app = FastAPI()
# Método GET a la url "/"
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.get("/")
async def root():
# Retornar el mensaje bienvenido a FastAPI
    return {"message": "primer ejemplo Fast API"}


# Método GET
# ruta donde se encuentra nuestro archivo.
MEDIA_ROOT = os.path.expanduser("~/opt/proyectos/fastAPI/iris.csv")
# Método GET a la url "/iris/"
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.get("/iris/")
async def root():
    # Cargamos el dataset con ayuda de pandas:
    X_df = pd.read_csv(MEDIA_ROOT)
    # Lo transformamos a json:
    data = X_df.to_json(orient="index")
    data = json.loads(data)
    # Retornar el dataset
    return data

# MÉTODO POST
# Añadimos el modelo de datos:
class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str
# Creamos la función donde crearemos el dato:
# Método POST a la url "/insertData/"
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.post("/insertData/")
async def insertData(item: Iris):
    # Leemos el archivo iris.csv e
    # insertamos en la última línea los campos a insertar
    with open(MEDIA_ROOT, 'a', newline='') as csvfile:
        # Nombres de los campos:
        fieldnames = ['sepal_length', 'sepal_width', 'petal_length',
                    'petal_width', 'species']
        # escribir en el csv
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # insertar en la última fila:
        writer.writerow({'sepal_length': item.sepal_length,
                        'sepal_width': item.sepal_width,
                        'petal_length': item.petal_length,
                        'petal_width': item.petal_width,
                        'species': item.species})
    return item


# Método PUT
# Método PUT a la url "/updateData/" + el ID del último dato (150)
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.put("/updateData/{item_id}")
async def updateData(item_id: int, item: Iris):
    # Leemos el csv con ayuda de pandas:
    df = pd.read_csv(MEDIA_ROOT)
    # Modificamos el último dato con los valores que nos lleguen:
    df.loc[df.index[-1], 'sepal_length'] = item.sepal_length
    df.loc[df.index[-1], 'sepal_width'] = item.sepal_width,
    df.loc[df.index[-1], 'petal_length'] = item.petal_length,
    df.loc[df.index[-1], 'petal_width'] = item.petal_width,
    df.loc[df.index[-1], 'species'] = item.species
    # convertir a csv
    df.to_csv(MEDIA_ROOT, index=False)
    # Retornamos el id que hemos modificado y el dato en formato diccionario:
    return {"item_id": item_id, **item.dict()}


# Método DELETE
# Método DELETE a la url "/deleteData/"
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.delete("/deleteData/{item_id}")
async def deleteData(item_id: int):
    # Leemos el csv con ayuda de pandas:
    df = pd.read_csv(MEDIA_ROOT)
    # Eliminar la última fila
    df.drop(df.index[item_id], inplace=True)
    # convertir a csv
    df.to_csv(MEDIA_ROOT, index=False)
    return 'Eliminado'
