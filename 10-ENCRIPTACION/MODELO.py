# IMPORTATE: Pip previos a instalar ---> pip install pandas, pip install cryptography, pip install requests
import pandas as pd
from cryptography.fernet import Fernet
import requests
from io import StringIO

# CREAMOS FUNCION PARA ENCRIPTAR EL VALOR
def encriptar_valor(valor, fernet):
    return fernet.encrypt(valor.encode())

# CREAMOS FUNCION PARA ENCRIPTAR COLUMNAS DE TIPO OBJECT
    if col.name in columnas_encriptar:
        return col.apply(lambda x: encriptar_valor(x, fernet) if isinstance(x, str) else x)
    return col

def main():
    # INGRESAR EL URL DEL ARCHIVO CSV
    url_csv = 'https://raw.githubusercontent.com/Martinerramuspe/05-DATA_CSV/main/ejemplo.csv'
    # INGRESAR EL NOMNRE DE LA COLUMNA A ANALIZAR 
    columna_encriptar = 'col1'
    
    # Cargar el archivo CSV desde la URL 
    response = requests.get(url_csv)
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)
    
    # Generamos una clave de encriptación
    clave = Fernet.generate_key()
    fernet = Fernet(clave)
    
    # Sobreescribimos sobre otro dataframe
    df_encriptado = df.copy()
    
    # Encriptar la columna específica de tipo objeto en el DataFrame copiado
    df_encriptado[columna_encriptar] = encriptar_columnas(df_encriptado[columna_encriptar], [columna_encriptar], fernet)
    
    print("DataFrame Original:")
    print(df.head(3))
    print("\nDataFrame Encriptado:")
    print(df_encriptado.head(3))
    
    # Descarga en un archivo CSV
    df_encriptado.to_csv('df_encriptado.csv', index=False)
    print("DataFrame Encriptado guardado en df_encriptado.csv")

if __name__ == "__main__":
    main()
