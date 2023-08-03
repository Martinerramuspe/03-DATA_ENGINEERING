# IMPORTANTE:instalar en consola "pip install pandas" Y "pip install cryptography".
import pandas as pd
from cryptography.fernet import Fernet

# CREAMOS DATAFRAME CASERO, CON DATOS SENCIBLES.
data = {'nombres': ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Pedro Gómez']}
df = pd.DataFrame(data)

df.head(5)
df.info()

# GENERAMOS CLAVE DE ENCRIPTACION Y CREAMOS OBJETO "Fernet"
clave = Fernet.generate_key()
fernet = Fernet(clave)

# CAMUFLAMOS LOS NOMBRES
nombres_originales = df['nombres'].tolist()
nombres_camuflados = [fernet.encrypt(nombre.encode()) for nombre in nombres_originales]

# AGREGAMOS LOS NOMBRES CAMUFLADOS AL DATAFRAME
df['nombres_camuflados'] = nombres_camuflados
df.head() # otra opcion es entregarles el Id, pero es un dato que esta expuesto dentro de la empresa, por lo cual es riesgoso.

# ACONDICIONAMOS DATAFRAME PARA ENTREGAR A "EMPRESA B", CONSIDERANDO QUE AHORA ESTAMOS EN LA "EMPRESA A"
df_empresa_B = df.drop(columns=['nombres'])

#02/08/2023 SE HACE ENTREGA DEL DF  A LA "EMPRESA B"
df_empresa_B.head(5)

#LA "EMPRESA B", VA ELIMINAR LOS 3 ULTIMAS FILAS
df_empresa_C = df_empresa_B.drop(index=df.index[-3:])

#03/08/2023 SE HACE ENTREGA DEL DF  A LA "EMPRESA C"
df_empresa_C.head(2)

#ESTA EMPRESA C" SE VA A ENCARGAR DE INCOOPORAR LOS SALDOS QUE VAN COBRAR ESTA LISTA DE PERSONAL.
df_empresa_A = df_empresa_C.copy()
df_empresa_A.head(2)
salario = [100000, 20000]
df_empresa_A['saldo'] = salario

#04/08/2023 FINALMENTE SE HACE ENTREGA A LA "EMPRESA A"
df_empresa_A.head(2)
df_empresa_A1 = df_empresa_A.copy()
df_empresa_A1.head(2)

# SE PROCEDE A DESENCRIPITAR LOS NOBRES 
nombres_camuflados = df_empresa_A1['nombres_camuflados'].tolist()
nombres_desencriptados = [fernet.decrypt(nombre).decode() for nombre in nombres_camuflados]

# AGREGAMOS LOS NOMBRES DESENCRITAMOS AL DATAFRAME.
df_empresa_A1['nombres_desencriptados'] = nombres_desencriptados
df_empresa_A1.head()

#AHORA LA "EMPRESA A" PUEDE CONTINUAR CON SUS ACTIVIDADES SIN HABER ARRIESGADO SUS DATOS SENCIBLES.