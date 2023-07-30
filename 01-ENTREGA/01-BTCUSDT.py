
# PREVIO A EJECUTAR ESTE SCRIPT, DEBEMOS INGRESAR A LA TERMINAL HE INSTALAR LO SIGUIENTE: pip install ccxt,pip install pandas,pip install sqlalchemy, pip install pymysql.
import pandas as pd
import ccxt
exchange = ccxt.binance()
bars = exchange.fetch_ohlcv("BTC/USDT", timeframe = "5m", limit =500)
df = pd.DataFrame(bars,columns=["time","open","high","low","close","volumen"])
print(df)
df.head(4)
df.info()

# Procedemos a interactuar el "df" con la base de datos "binance" creada en Mysql.

from sqlalchemy import create_engine

# Con este codigo, establecemos conexion con la base de datoss.
engine = create_engine('mysql+pymysql://root:siempreeshoy12@localhost/binance')

# Volcar los datos a la tabla en MySQL, ACLARACION: sqlalchemy TAMBIEN se encarga de CREAR LA tabla en mysql, con las restricciones.
df.to_sql(name='tabla', con=engine, if_exists='append', index=False)

# Comando para cerrar la conexión
engine.dispose()







