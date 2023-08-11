#IMPORTANTE: Pip previso a instalar son  "pip install pandas", "pip install cryptography", "pip install requests"
import os
import pandas as pd
from cryptography.fernet import Fernet
import requests
from io import StringIO

# Recibe los vallores pasados como variables de entorno
url_csv = os.environ.get('URL_CSV')
columnas_encriptar = os.environ.get('COLUMNAS_ENCRIPTAR').split(',')

# Cargar el archivo CSV desde la URL 
response = requests.get(url_csv)
csv_data = StringIO(response.text)
df = pd.read_csv(csv_data)

# Generamos una clave de encriptación
clave = Fernet.generate_key()
fernet = Fernet(clave)

# Función para encriptar un valor
def encriptar_valor(valor):
    return fernet.encrypt(valor.encode())

# Función para encriptar columnas de tipo objeto
def encriptar_columnas(col, columnas_encriptar):
    if col.name in columnas_encriptar:
        return col.apply(lambda x: encriptar_valor(x) if isinstance(x, str) else x)
    return col

# Sobreescribimos sobre otro dataframe
df_encriptado = df.copy()

# Encriptar las columnas específicas de tipo objeto en el DataFrame copiado
df_encriptado = df_encriptado.apply(lambda col: encriptar_columnas(col, columnas_encriptar))

print("DataFrame Original:")
print(df.head(3))

print("\nDataFrame Encriptado:")
print(df_encriptado.head(3))

# Descarga  en un archivo CSV
df_encriptado.to_csv('/app/data/df_encriptado.csv', index=False)
print("DataFrame Encriptado guardado en df_encriptado.csv")


#DOCKER:
#IMPORTANTE: PARA REALIZAR LA LLAMADA DOCKER DESDE CUALQUIER TERMINAL----->   docker run -v C:\Users\erram\DirectorioLocal:/app/data -e URL_CSV="https://raw.githubusercontent.com/Martinerramuspe/05-DATA_CSV/main/estadistica.csv" -e COLUMNAS_ENCRIPTAR="Colum1, Colum2" -it data_encryption
#IMPORTANTE: VAS A NECESITAR COMO DATO DE ENTRADA EL URL (Ubicacion del csv en github, acordate de agregarle el "raw")
#IMPORTANTE: VAS A NECESITAR COMO DATO DE ENTRADA EL NOMBRE DE LAS COLUMNAS A TRANSFORMAR (Estas tienen que ser solo de tipo "object").
#IMPORTANTE: UNA VEZ QUE SE EJECUTA DE FORMA CORRECTA EL MODELO, AUTOMATICAMENTE SE DESCARGA UN ARCHIVO CSV. CON LA ENCRIPTACION.