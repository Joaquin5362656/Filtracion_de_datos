import leer
import limpiar
import analizar
import visualizar

def main():
    # Carga ls datos
    datos_cargados = leer.leer_datos('ventas.csv')
    
    # Limpia datos
    datos_limpios = limpiar.limpiar_datos(datos_cargados)

    
    # Para visualizar datos
    visualizar.ventasXtiempo(datos_limpios)
    visualizar.ventasXproducto(datos_limpios)
    visualizar.distribucionXventas(datos_limpios)

if __name__ == "__main__":
    main()
