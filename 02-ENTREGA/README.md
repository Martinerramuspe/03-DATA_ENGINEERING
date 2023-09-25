# Extracción y Carga de Datos desde Google Drive

Este proyecto tiene como fin, extraer datos estructurados de una hoja de cálculo de Google Sheets alojada en Google Drive y transformarlos antes de cargarlos en una base de datos local según necesidades específicas.

![](https://github.com/Martinerramuspe/PICTURE/blob/main/sheets.png)

## Objetivo del Proyecto

El propósito principal de este proyecto es automatizar el proceso de extracción, transformación y carga (ETL) de datos desde Google Drive hacia una base de datos local utilizando un script de Python. Esto facilita la gestión y análisis de datos provenientes de hojas de cálculo en la nube.
## Proceso ETL

1. **Autenticación de Credenciales**: Se importan y autentican las credenciales de Google para acceder a Google Drive y Sheets.

2. **Extracción de Datos**: Los datos estructurados se leen e importan desde Google Drive a Python utilizando la API de Google.

3. **Transformación de Datos**: Los datos se transforman según los requisitos del proyecto. Esto puede incluir limpieza, formatos de fecha u otras transformaciones necesarias.

4. **Carga en la Base de Datos**: Los datos transformados se cargan en una base de datos local PostgreSQL utilizando SQLAlchemy. La tabla se crea automáticamente a partir de los datos.

## Instrucciones de Uso

Antes de utilizar el script `MODELO.py`, sigue estos pasos:

1. **Configuración de Credenciales Google**: Asegúrate de que las credenciales de Google necesarias para acceder a Google Drive y Google Sheets estén correctamente configuradas. Esto incluye la obtención de un archivo JSON de credenciales desde [enlace a la consola de desarrolladores de Google](https://console.cloud.google.com/apis/credentials) y la autorización de acceso a la hoja de cálculo. Asegúrate de tener estas credenciales disponibles y listas antes de ejecutar el script.

2. **Dependencias**: Asegúrate de que todas las bibliotecas y dependencias necesarias estén instaladas. Puedes instalarlas utilizando `pip` con el comando:

   ```bash
   pip install pandas gspread oauth2client sqlalchemy psycopg2 requests
