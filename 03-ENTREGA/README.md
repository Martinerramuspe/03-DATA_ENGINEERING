# DAG de Apache Airflow para Cargar Datos desde Binance a Redshift

Este proyecto utiliza Apache Airflow para automatizar la carga de datos desde Binance a una base de datos Redshift. El DAG (Directed Acyclic Graph) consta de dos tareas principales: la creación de un DataFrame desde los datos de Binance y la carga de este DataFrame en Redshift.

![](https://github.com/Martinerramuspe/PICTURE/blob/main/redshift.png)

Además, este proyecto incluye una implementación de Docker para facilitar el entorno de ejecución de Apache Airflow y garantizar una configuración consistente.

## Objetivo del Proyecto

El objetivo principal de este proyecto es proporcionar una automatización robusta y programada para obtener datos de Binance y cargarlos en una base de datos Redshift. Esto facilita la obtención y análisis de datos financieros en tiempo real.

## Tareas del DAG

### Tarea 1: Crear DataFrame desde Binance

- **Descripción**: Esta tarea utiliza la biblioteca ccxt para obtener datos de Binance, específicamente los precios OHLCV para el par de negociación "BTC/USDT" en un marco de tiempo de 5 minutos. Luego, crea un DataFrame a partir de estos datos y lo guarda en un archivo temporal CSV.

- **Python Operator**: PythonOperator ejecuta la función `create_dataframe` para realizar esta tarea.

### Tarea 2: Cargar DataFrame en Redshift

- **Descripción**: Esta tarea carga el DataFrame creado en la Tarea 1 en una base de datos Redshift. Antes de cargar los datos, realiza una transformación simple en el DataFrame cambiando el nombre de la columna "open" a "open_price". Luego, utiliza SQLAlchemy para conectarse a Redshift y cargar los datos en una tabla llamada "pietroboni".

- **Python Operator**: PythonOperator ejecuta la función `load_to_redshift` para realizar esta tarea.

## Implementación de Docker

Este proyecto incluye una implementación de Docker para facilitar la configuración y ejecución de Apache Airflow junto con las dependencias necesarias. Los siguientes archivos se proporcionan para la construcción de la imagen Docker:

![](https://github.com/Martinerramuspe/PICTURE/blob/main/AIRFLOW.png)


- `Dockerfile`: Define las instrucciones para construir la imagen Docker de Apache Airflow y sus dependencias.

- `docker-compose.yaml`: Define la configuración de los contenedores Docker, incluyendo el contenedor de Apache Airflow y los servicios de base de datos necesarios.

- `requirements.txt`: Lista

