###                    MODELO ENCRIPTACION
Este MODELO es una solución para encriptar datos en archivos CSV de forma segura. Utiliza la biblioteca cryptography y el algoritmo Fernet para proteger columnas específicas de un archivo CSV mediante encriptación. El MODELO recibe la URL del archivo CSV y el nombre de las columnas a encriptar como variables de entorno. Luego, carga el CSV desde la URL, genera una clave de encriptación y aplica la encriptación a las columnas especificadas. El resultado se almacena en un nuevo archivo CSV encriptado. El uso de Docker facilita la ejecución del script en cualquier entorno. Para usarlo, se debe ejecutar un contenedor Docker con los argumentos necesarios: la URL del CSV y las columnas a encriptar.

This MODEL offers a solution for securely encrypting data in CSV files. It utilizes the cryptography library and the Fernet algorithm to ensure the protection of specific columns within a CSV file through encryption. The MODEL takes input parameters such as the URL of the CSV file and the names of the columns that need to be encrypted, treating them as environmental variables. Subsequently, the model loads the CSV data from the provided URL, generates an encryption key, and applies encryption to the specified columns. The output is stored in a new CSV file with encryption applied. The use of Docker simplifies the execution of the script across various environments. To utilize it, one needs to execute a Docker container with the required arguments: the CSV URL and the columns intended for encryption.

 ![](https://github.com/Martinerramuspe/PICTURE/blob/main/ENCRIPTACION.png)