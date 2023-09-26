# DAG de Apache Airflow para Extracción, Carga y Notificación

Este DAG de Apache Airflow tiene como objetivo realizar varias tareas relacionadas con la extracción de datos de Binance, la carga de datos en Redshift y el envío de notificaciones por correo electrónico. Asegúrate de seguir los pasos a continuación antes de ejecutar el DAG.

![](https://github.com/Martinerramuspe/PICTURE/blob/main/etl.png)

## Tareas del DAG

El DAG consta de las siguientes tareas:

### Tarea 1: Crear DataFrame desde Binance

- **Descripción**: Esta tarea utiliza la biblioteca ccxt para obtener los datos OHLCV (Open, High, Low, Close, Volumen) para el par de negociación "BTC/USDT" en un marco de tiempo de 5 minutos desde Binance. Luego, crea un DataFrame de pandas a partir de estos datos y lo guarda en un archivo temporal CSV.

### Tarea 2: Cargar DataFrame en Redshift

- **Descripción**: Esta tarea carga el DataFrame creado en la Tarea 1 en una base de datos Redshift. Antes de cargar los datos, realiza una transformación simple cambiando el nombre de la columna "open" a "open_price". Luego, utiliza SQLAlchemy para conectarse a Redshift y cargar los datos en una tabla llamada "casas". Asegúrate de configurar la cadena de conexión de Redshift en la sección `load_to_redshift`.

### Tarea 3: Verificar Condición

- **Descripción**: Esta tarea verifica si la condición "low > 25500" se cumple en los datos del DataFrame. Si la condición se cumple, devuelve "True", de lo contrario, devuelve "False".

### Tarea 4: Enviar Correo Electrónico

- **Descripción**: Esta tarea envía un correo electrónico si la condición verificada en la Tarea 3 es "True". El remitente, destinatario, asunto y cuerpo del mensaje se configuran en esta tarea. Asegúrate de configurar las credenciales de correo electrónico en la sección `enviar_correo` y ajustar los valores de correo electrónico según sea necesario.

## Requisitos Previos

Antes de ejecutar este DAG, debes asegurarte de que todas las bibliotecas y dependencias necesarias estén instaladas en tu entorno de Python. Puedes instalarlas utilizando `pip` con el siguiente comando:

```bash
pip install ccxt pandas sqlalchemy psycopg2-binary
