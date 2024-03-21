def analizar_datos(data):
    """
    Esta funcion realiza un análisis de los datos de ventas que se le pasan como argumento.
    Usa la funcion .groupby() para agrupar los datos por columna 'producto' y despues sumarlos 
    retorna la suma de los productos
    """
    ventas_sumadas = data.groupby('producto').sum()
    return ventas_sumadas
