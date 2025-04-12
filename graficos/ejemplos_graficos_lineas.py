# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt  # Principal biblioteca para gráficos
import numpy as np  # Para manejo de arrays y operaciones matemáticas
from datetime import datetime, timedelta  # Para trabajar con fechas, es una biblioteca nativa de python

# Configuración para mostrar caracteres especiales (tildes, ñ) correctamente
plt.rcParams['font.family'] = 'sans-serif'  # Tipo de fuente
plt.rcParams['font.sans-serif'] = ['Arial']  # Fuente específica

def grafico_simple():
    """Función que crea un gráfico lineal básico"""
    # Creamos dos arrays con los datos para X e Y
    x = np.array([1, 2, 3, 4, 5])  # Valores para el eje X
    y = np.array([2, 4, 6, 8, 10])  # Valores para el eje Y

    # Creamos una nueva figura con un tamaño específico (ancho: 10, alto: 6)
    plt.figure(figsize=(10, 6))
    
    # Dibujamos la línea: 'b-' significa línea azul sólida
    # label es el texto que aparecerá en la leyenda
    plt.plot(x, y, 'b-', label='Línea simple')
    
    # Añadimos título y etiquetas a los ejes
    plt.title('Gráfico Lineal Simple')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    
    plt.grid(True)  # Añadimos una cuadrícula
    plt.legend()    # Mostramos la leyenda
    
    # Guardamos el gráfico como imagen PNG
    plt.savefig('graficos/grafico_simple.png')
    plt.close()  # Cerramos la figura para liberar memoria

def grafico_multiple():
    """Función que crea un gráfico con múltiples líneas"""
    # Datos para el eje X
    x = np.array([1, 2, 3, 4, 5])
    
    # Diferentes cálculos para cada línea
    y1 = x * 2          # Línea recta (función lineal)
    y2 = x ** 2        # Parábola (función cuadrática)
    y3 = np.log(x)     # Función logarítmica

    plt.figure(figsize=(10, 6))
    
    # Dibujamos tres líneas diferentes:
    # 'b-' = línea azul sólida
    # 'r--' = línea roja discontinua
    # 'g:' = línea verde punteada
    plt.plot(x, y1, 'b-', label='Lineal')
    plt.plot(x, y2, 'r--', label='Cuadrática')
    plt.plot(x, y3, 'g:', label='Logarítmica')
    
    plt.title('Múltiples Líneas')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid(True)
    plt.legend()
    
    plt.savefig('graficos/grafico_multiple.png')
    plt.close()

def grafico_estilos():
    """Función que muestra diferentes estilos de líneas"""
    # Creamos 100 puntos espaciados uniformemente entre 0 y 10
    x = np.linspace(0, 10, 100)
    
    plt.figure(figsize=(12, 8))
    
    # Dibujamos la misma función (seno) con diferentes estilos y desfases
    plt.plot(x, np.sin(x), 'b-', label='Sólida')          # Línea sólida
    plt.plot(x, np.sin(x+1), 'r--', label='Discontinua')  # Línea discontinua
    plt.plot(x, np.sin(x+2), 'g:', label='Punteada')      # Línea punteada
    plt.plot(x, np.sin(x+3), 'm-.', label='Punto y raya') # Línea punto-raya
    
    plt.title('Diferentes Estilos de Líneas')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid(True)
    plt.legend()
    
    plt.savefig('graficos/grafico_estilos.png')
    plt.close()

def grafico_tiempo():
    """Función que crea un gráfico con datos temporales"""
    # Creamos una lista de fechas (10 días consecutivos desde hoy)
    fechas = [datetime.now() + timedelta(days=x) for x in range(10)]
    # Creamos valores (cuadrados de los números del 0 al 9)
    valores = [x**2 for x in range(10)]

    plt.figure(figsize=(12, 6))
    # 'b-o' significa línea azul sólida con marcadores circulares
    plt.plot(fechas, valores, 'b-o')
    
    plt.title('Datos a lo Largo del Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Valor')
    plt.grid(True)
    
    # Rotamos las etiquetas del eje X para mejor legibilidad
    plt.xticks(rotation=45)
    
    # Ajustamos el diseño para que no se corten las etiquetas
    plt.tight_layout()
    
    plt.savefig('graficos/grafico_tiempo.png')
    plt.close()

def grafico_personalizado():
    """Función que crea un gráfico con personalización avanzada"""
    # Creamos datos usando la función seno
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Creamos una figura con fondo gris claro
    plt.figure(figsize=(12, 8), facecolor='#f0f0f0')
    
    # Creamos un gráfico altamente personalizado:
    plt.plot(x, y,
            color='#FF5733',        # Color en hexadecimal
            linewidth=2,            # Grosor de línea
            linestyle='-',          # Estilo de línea
            marker='o',             # Tipo de marcador
            markersize=6,           # Tamaño de marcador
            markerfacecolor='white',# Color de relleno del marcador
            markeredgecolor='#FF5733', # Color del borde del marcador
            markeredgewidth=2,      # Grosor del borde del marcador
            label='Datos')          # Etiqueta para la leyenda

    # Personalizamos títulos y etiquetas
    plt.title('Gráfico Personalizado', fontsize=16, pad=20)
    plt.xlabel('Eje X', fontsize=12)
    plt.ylabel('Eje Y', fontsize=12)
    
    # Personalizamos la cuadrícula
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Establecemos límites para los ejes
    plt.xlim(-0.5, 10.5)
    plt.ylim(-1.5, 1.5)
    
    # Añadimos una leyenda con sombra
    plt.legend(loc='upper right', facecolor='white', framealpha=1, shadow=True)
    
    # Ajustamos los márgenes
    plt.tight_layout()
    
    # Guardamos con alta resolución (300 dpi)
    plt.savefig('graficos/grafico_personalizado.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Función principal que ejecuta todos los ejemplos"""
    print("Generando gráficos...")
    
    # Ejecutamos cada función y mostramos mensaje de confirmación
    grafico_simple()
    print("✓ Gráfico simple generado")
    
    grafico_multiple()
    print("✓ Gráfico múltiple generado")
    
    grafico_estilos()
    print("✓ Gráfico de estilos generado")
    
    grafico_tiempo()
    print("✓ Gráfico temporal generado")
    
    grafico_personalizado()
    print("✓ Gráfico personalizado generado")
    
    print("\nTodos los gráficos han sido guardados en la carpeta 'graficos'")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
