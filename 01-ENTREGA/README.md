# Script de Extracción y Carga de Datos desde Binance a MySQL

Este script tiene como objetivo extraer datos históricos de precios de Binance para el par de negociación "BTC/USDT" y cargarlos en una base de datos MySQL. Asegúrate de seguir los pasos a continuación antes de ejecutar el script.

![](https://github.com/Martinerramuspe/PICTURE/blob/main/VELAS_JAPNESAS.jpg)

## Proceso:
1 **Extracción de Datos desde Binance**: Utiliza la biblioteca ccxt para acceder a la API de Binance y obtener los datos OHLCV (Open, High, Low, Close, Volumen) para el par de negociación "BTC/USDT" en un marco de tiempo de 5 minutos. Los datos se almacenan en un DataFrame de pandas y se muestran en la consola.

2 **Conexión a la Base de Datos MySQL**: El script se conecta a una base de datos MySQL utilizando SQLAlchemy. Asegúrate de que la base de datos "binance" esté configurada y accesible en tu servidor MySQL local.

3 **Carga de Datos en MySQL**: El DataFrame se vuelca en una tabla llamada "tabla" en la base de datos MySQL. Si la tabla no existe, SQLAlchemy la creará automáticamente con las restricciones adecuadas.

4 **Cierre de la Conexión**: Finalmente, el script cierra la conexión a la base de datos MySQL.

## Requisitos Previos

Antes de ejecutar este script, debes asegurarte de que todas las bibliotecas y dependencias necesarias estén instaladas en tu entorno de Python. Puedes instalarlas utilizando `pip` con el siguiente comando:

```bash
pip install ccxt pandas sqlalchemy pymysql

