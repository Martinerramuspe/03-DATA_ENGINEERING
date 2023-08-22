from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from sqlalchemy import create_engine

def extract_data():
    json_url = "https://raw.githubusercontent.com/Martinerramuspe/06-ADJUNTOS/main/prueba.json"
    response = requests.get(json_url)
    google_credentials = json.loads(response.text)
    
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(google_credentials, scope)
    client = gspread.authorize(credentials)
    
    worksheet = client.open('Pinguinos').sheet1 
    data = worksheet.get_all_values()
    return data

def process_data():
    data = extract_data()
    df = pd.DataFrame(data[1:], columns=data[0])
    df.drop_duplicates(inplace=True)
    df.insert(0, 'Id', range(1, len(df) + 1))
    current_datetime = datetime.now()
    df['Registro'] = current_datetime
    json_string = df.to_json()  # Convertir DataFrame a JSON ,Airflow no procesa Dataframe grandes!
    return json_string


def load_to_postgres(json_string):
    df = pd.read_json(json_string)
    connection_url = 'postgresql://postgres:1540794222@localhost:5432/Datalake'
    engine = create_engine(connection_url)
    nombre_tabla = 'extraccion'
    df.to_sql(nombre_tabla, engine, if_exists='replace', index=False)

default_args = {
    'owner': 'DavidBU',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    default_args=default_args,
    dag_id='dag_extraccion_carga',
    start_date=datetime(2023, 8, 20),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = PythonOperator(
        task_id='primera_operacion',
        python_callable=extract_data
    )

    task2 = PythonOperator(
        task_id='segunda_operacion',
        python_callable=process_data
    )

    task3 = PythonOperator(
        task_id='tercera_operacion',
        python_callable=load_to_postgres,
        op_args=[task2.output],
        provide_context=True
    )

# Definir la tarea PostgresOperator para ejecutar SQL
task4 = PostgresOperator(
    task_id='tercera_operacion_sql',
    sql="SELECT * FROM my_table",
    postgres_conn_id="my_postgres_connection",
    autocommit=True
)

# Definir las dependencias entre las tareas
task1 >> task2 >> [task3, task4]


    
 
    
   