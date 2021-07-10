1. Crear entorno virtual:
virtualenv fastAPI_env

2. activar entorno virtual:
source fastAPI_env/bin/activate

3. Instalar paquetes necesarios:
pip install fastapi
pip install pandas
pip install uvicorn[standard]
pip install autopep8
pip install falke8

4.Ejecutar servidor web:
uvicorn main:app --reload

5. Mostrar métodos permitidos:
http://127.0.0.1:8000/docs
