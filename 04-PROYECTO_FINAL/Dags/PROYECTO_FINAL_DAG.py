from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from sqlalchemy import create_engine
import tempfile
import os
import ccxt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_dataframe(**kwargs):
    exchange = ccxt.binance()
    bars = exchange.fetch_ohlcv("BTC/USDT", timeframe="5m", limit=10)
    df = pd.DataFrame(bars, columns=["time", "open", "high", "low", "close", "volume"])
    
    # Guarda el DataFrame en un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
        df.to_csv(temp_file.name, index=False)
        kwargs['ti'].xcom_push(key='temp_file_path', value=temp_file.name)

def load_to_redshift(**kwargs):
    temp_file_path = kwargs['ti'].xcom_pull(task_ids='create_dataframe_task', key='temp_file_path')
    
    # Lee el DataFrame desde el archivo temporal
    df = pd.read_csv(temp_file_path)
    
    # Cambia el nombre de la columna "open" a "open_price"
    df.rename(columns={'open': 'open_price'}, inplace=True)
    
    # Cadena de conexión de Redshift
    redshift_connection_string = "postgresql://arturomontesdeoca4892_coderhouse:AqiS616AWa@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/dev"

    # Crea un motor de SQLAlchemy para la conexión
    engine = create_engine(redshift_connection_string)

    # Convierte el DataFrame a una tabla en Redshift
    table_name = 'casas'
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    # Cierra la conexión de SQLAlchemy
    engine.dispose()

def verificar_condicion(**kwargs):
    temp_file_path = kwargs['ti'].xcom_pull(task_ids='create_dataframe_task', key='temp_file_path')
    df = pd.read_csv(temp_file_path)
    
    condicion_cumplida = (df['low'] > 25500).any()
    resultado = 'True' if condicion_cumplida else 'False'
    
    return resultado

def enviar_correo(**kwargs):
    ti = kwargs['ti']
    condicion_cumplida = ti.xcom_pull(task_ids='verificar_condicion')
    
    if condicion_cumplida == 'True':
        remitente = 'erramuspe14@gmail.com'
        destinatario = 'merramuspe@llpietroboni.com.ar'
        asunto = 'CONDICIÓN CUMPLIDA'
        cuerpo_mensaje = 'Felicitaciones'
        
        # Configurar el correo
        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = destinatario
        mensaje['Subject'] = asunto
        
        # Agregar el cuerpo del mensaje
        mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))
        
        # Conexión al servidor SMTP y envío del correo
        try:
            servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
            servidor_smtp.starttls()
            servidor_smtp.login(remitente, '2991erramuspe')  
            servidor_smtp.sendmail(remitente, destinatario, mensaje.as_string())
            servidor_smtp.quit()
            print('Correo enviado con éxito')
        except Exception as e:
            print('Error al enviar el correo:', str(e))

default_args = {
    'owner': 'DavidBU',
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    default_args=default_args,
    dag_id='BINANCE_MAIL_REDSHIFT',
    start_date=datetime(2023, 9, 12),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = PythonOperator(
        task_id='create_dataframe_task',
        python_callable=create_dataframe,
        provide_context=True
    )
    
    task2 = PythonOperator(
        task_id='load_to_redshift_task',
        python_callable=load_to_redshift,
        provide_context=True
    )

    task3 = PythonOperator(
        task_id='verificar_condicion',
        python_callable=verificar_condicion,
        provide_context=True
    )
    
    task4 = PythonOperator(
        task_id='enviar_correo_task',
        python_callable=enviar_correo,
        provide_context=True
    )

    task1 >> [task2, task3]  
    task2 >> task4  
    task3 >> task4  
