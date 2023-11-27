# IMPORTANTE: PipS previos a instalar----> pip install pandas, pip install gspread , pip install oauth2client, pip install sqlalchemy, pip install psycopg2 , pip install requests
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine
import json
import requests
from datetime import datetime

# Cargar las credenciales desde el archivo JSON en GitHub
json_url = "https://raw.githubusercontent.com/Martinerramuspe/04-ADJUNTOS/main/prueba.json" #importante el "raw"
response = requests.get(json_url)
google_credentials = json.loads(response.text)

# CONFIGURACIONES DE AUTENTICACION
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict(google_credentials, scope)
client = gspread.authorize(credentials)


# IMPORTANTE: Tener bien definido el nombre del "excel sheet" (no .xlsx), Ubicado en drive.
# IMPORTANTE: El excel sheet en drive, debe ser compartido por el usuario : "prueba-cuenta@prueba-proyecto-394607.iam.gserviceaccount.com" ,para ser elevado en python.
worksheet = client.open('Pinguinos').sheet1 

# OBTEJER VALORES DE HOJAA SHEET.
data = worksheet.get_all_values()

# CONVERTIR EN DATAFRAME
df = pd.DataFrame(data[1:], columns=data[0])

# ELIMINAR FILAS DUPLICADAS DIRECTAMENTE EN EL DATAFRAME ORIGINAL
df.drop_duplicates(inplace=True)

# AGREGAMOS UN IDENTIFICADOR
df.insert(0, 'Id', range(1, len(df) + 1))

# AGREGAMOS UNA COLUMNA DE AUDITORIA
current_datetime = datetime.now()
df['Registro'] = current_datetime

# OBSERVAMOS RESULTADOS
df.head(2)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CONECTAMOS A BASE DE DATOS LOCAL EN PostgreSQL.
connection_url = 'postgresql://postgres:1540794222@localhost:5432/Datalake'

# CONEXION A LA BASE DE DATOS
engine = create_engine(connection_url)

# DESIGNAMOS NOMBRE A LA NUEVA TABLA
nombre_tabla = 'extraccion'

# TRASLADAMOS DEL DATAFRAME A LA BASE 
# IMPORTATE: Increiblemente "df.to_sq" se encarga de crear la tabla en la base de datos automaticamente, identificando el tipo de dato de cada columna.
df.to_sql(nombre_tabla, engine, if_exists='replace', index=False)

