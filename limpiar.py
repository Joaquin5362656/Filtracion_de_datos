def limpiar_datos(datos):
    """Esta funcion se encarga de limpiar los datos, con el data.dropna() eliminamos filas con valores nulos
    Retorna el dataframe limpio (sin filas con valores nulos)"""
    cleaned_data = datos.dropna() 
    return cleaned_data
