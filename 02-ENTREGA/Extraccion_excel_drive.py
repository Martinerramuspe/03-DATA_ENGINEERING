# IMPORTANTE: Pip previos a instalar, "pip install pandas", "pip install gspread" , "pip install oauth2client","pip install sqlalchemy psycopg2"

import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# DEFINIR ALCANCE Y CARGA DE CREDENCIAL.
# IMPORTANTE: Tener bien definido la ubicacion del archivo ".json" en tu pc. 
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\erram\\Downloads\\prueba.json', scope) 
client = gspread.authorize(credentials)


# IMPORTANTE: Tener bien definido el nombre del excel sheet, Ubicado en drive.
worksheet = client.open('ghfghfgh').sheet1

# OBTEJER VALORES DE HOJAA.
data = worksheet.get_all_values()

# CONVERTIR EN DATAFRAME
df = pd.DataFrame(data[1:], columns=data[0])


# CREAMOS NUEVO DATAFRAME, QUE ELIMINE LAS FILAS DUPLICADAS.
df_sin_duplicados = df.drop_duplicates()

df_sin_duplicados.head(2)

#CONECTAMOS A BASE DE DATOS EN PostgreSQL


from sqlalchemy import create_engine
connection_url = 'postgresql://postgres:1540794222@localhost:5432/Datalake'
# CONEXION A LA BASE DE DATOS
engine = create_engine(connection_url)

# DESIGNAMOS NOMBRE A LA NUEVA TABLA
nombre_tabla = 'extraccion'

# TRASLADAMOS DEL DATAFRAME A LA BASE 
df.to_sql(nombre_tabla, engine, if_exists='replace', index=False)

