import matplotlib.pyplot as plt


def ventasXtiempo(datos):
    """
    Esta función recibe un DataFrame datos que contiene información de ventas a lo largo del tiempo. 
    Utiliza la función plt.plot() para trazar un gráfico de línea que muestra cómo cambian 
    las ventas a lo largo del tiempo.
    Por ultimo, muestra el grafico
    """
    plt.plot(datos['fecha'], datos['cantidad'] * datos['precio'])
    plt.xlabel('Fecha')
    plt.ylabel('Ventas')
    plt.title('Ventas a lo largo del tiempo')
    plt.show()

def ventasXproducto(datos):
    """ 
    Esta funcion recibe una DataFrame datos que contiene informacion de ventas por productos.
    Utiliza la función plt.bar() para trazar un gráfico de barras que muestra las ventas 
    totales de cada producto, rota 45 grados el grafico para que sea mas legible.
    Por ultimo, muestra el grafico
    """
    plt.bar(datos['producto'], datos['cantidad'] * datos['precio'])
    plt.xlabel('Producto')
    plt.ylabel('Ventas')
    plt.title('Ventas por producto')
    plt.xticks(rotation=45)
    plt.show()

def distribucionXventas(datos):
    """
    La función recibe un DataFrame datos que contiene información de ventas. 
    Utiliza la función plt.hist() para trazar un histograma que muestra la distribución de las ventas totales.  
    Por ultimo, muestra el grafico
    """
    plt.hist(datos['cantidad'] * datos['precio'], bins=10)
    plt.xlabel('Ventas')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de ventas')
    plt.show()
