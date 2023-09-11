## RESUMEN: Considerando las correcciones, procedimos a realizar un Dag mas sencillas que cumpla con lo solicitado.

- El "Dag7.py" que se presents en esta correciones, Consta de task1 >> task2.
  
- task1: Se importa informacion correspondiente a precio de BTC y se lo transforma en dataframe para su manipulacion.
  
- task2: Se carga la informacion estrcturada en la base de datos de redssfhit.
  
- ACLARACION: Sabemos que la manipulacion de dataframe entre tasks , no es muy aceptada por airflow. Por lo que en este caso usamos Xcom , para llevar a cabo la comunicacion.
  
- Añadimos Dockerfile y requirements.txt para crear un entorno seguro , ya que se usan muchas bibliotecas con version especificas a respetar.


## PROCESO EJECUCION:
  
- Descargando todo el contenido y ubicarlo sobre algun durectorio.
- ejecutar en la terminal, estando sobre el directorio : "docker-compose up --build"
- Acceder a http://localhost:8080/  , Usuario: airflow , contraseña: airflow.
- Finalmente, administrar  funcionamiento del Dag7.py. desde la plataforma.

