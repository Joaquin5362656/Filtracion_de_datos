import pandas as pd

def leer_datos(archivo):
    """
    Funcion que lee el archivo csv con pandas y devuelve los datos como un DataFrame de pandasa
    """
    return pd.read_csv(archivo)
