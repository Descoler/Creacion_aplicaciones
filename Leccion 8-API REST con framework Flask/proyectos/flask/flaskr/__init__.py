# Librerías para crear la aplicación y recoger los datos:
from flask import Flask, request
import pandas as pd
import csv
import json

# Creamos nuestra primera aplicación llamada app.
# Creamos "__name__" como función principal
app = Flask(__name__)

# Ruta de inicio "/", metodo GET
@app.route('/', methods=['GET'])
def home():
    #Mensaje que aparecerá en la ventana
    return "Bienvenido a FLASK"

# Ruta de inicio "/iris", metodo GET
@app.route('/iris', methods=['GET'])
def irisData():
    # Cargamos el dataset con ayuda de pandas:
    X_df = pd.read_csv('iris.csv')
    # Resumen del Dataset .describe():
    describe = X_df.describe().to_json(orient="index")
    describe = json.loads(describe)
    return describe


# Ruta de inicio "/insertData", metodo GET
@app.route('/insertData', methods=['POST'])
def insertdata():
    # definir 'data' como el conjunto de datos
    # que se reciben a través del Postman:
    data = request.data
    data = json.loads(data)
    # insertar dato en csv:
    with open('iris.csv', 'a', newline='') as csvfile:
        fieldnames = ['sepal_length', 'sepal_width', 'petal_length',
                    'petal_width', 'species']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'sepal_length': data['sepal_length'],
                    'sepal_width': data['sepal_width'],
                    'petal_length': data['petal_length'],
                    'petal_width': data['petal_width'],
                    'species': data['species']})
        print("writing complete")
    return data


# Ruta de inicio "/updateData", metodo PUT
@app.route('/updateData', methods=['PUT'])
def updatedata():
    # definir 'data' como el conjunto de datos
    # que se reciben a través del Postman:
    data = request.data
    data = json.loads(data)
    df = pd.read_csv('iris.csv')
    # sustituimos la última fila del dataset cada uno de los valores
    # con los datos que recibimos 'data':
    df.loc[df.index[-1], 'sepal_length'] = data['sepal_length']
    df.loc[df.index[-1], 'sepal_width'] = data['sepal_width']
    df.loc[df.index[-1], 'petal_length'] = data['petal_length']
    df.loc[df.index[-1], 'petal_width'] = data['petal_width']
    df.loc[df.index[-1], 'species'] = data['species']
    # convertir a csv
    df.to_csv('iris.csv', index=False)
    # mostrar el último dato en formato Json:
    result = df.iloc[-1].to_json(orient="index")
    return result


# Ruta de inicio "/deleteData", metodo DELETE
@app.route('/deleteData', methods=['DELETE'])
def deleteData():
    df = pd.read_csv('iris.csv')
    # Eliminar la última fila
    df.drop(df.index[-1], inplace=True)
    # convertir a csv
    df.to_csv('iris.csv', index=False)
    # mostrar el último dato en formato Json:
    result = df.iloc[-1].to_json(orient="index")
    return result


if __name__ == 'main':
    # Correr la aplicación inicializada
    app.run(debug=True)
