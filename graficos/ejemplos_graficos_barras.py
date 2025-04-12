# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt  # Para crear los gráficos
import numpy as np  # Para operaciones numéricas
from matplotlib import colors  # Para personalizar colores

# Configuración para mostrar caracteres especiales
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

def grafico_barras_simple():
    """Ejemplo de gráfico de barras básico"""
    # Datos para el gráfico
    categorias = ['A', 'B', 'C', 'D']  # Etiquetas para el eje X
    valores = [23, 45, 56, 78]        # Altura de cada barra

    # Crear la figura con un tamaño específico
    plt.figure(figsize=(10, 6))
    
    # Crear el gráfico de barras
    # plt.bar(x, height) - x: posición de las barras, height: altura
    plt.bar(categorias, valores, color='skyblue')
    
    # Personalización del gráfico
    plt.title('Gráfico de Barras Simple')  # Título
    plt.xlabel('Categorías')               # Etiqueta eje X
    plt.ylabel('Valores')                  # Etiqueta eje Y
    plt.grid(True, linestyle='--', alpha=0.7)  # Agregar cuadrícula
    
    # Guardar el gráfico
    plt.savefig('graficos/barras_simple.png')
    plt.close()  # Cerrar la figura para liberar memoria

def grafico_barras_multiple():
    """Ejemplo de gráfico con múltiples barras agrupadas"""
    # Datos para el gráfico
    categorias = ['Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4']
    valores1 = [20, 34, 30, 35]
    valores2 = [25, 32, 34, 20]
    valores3 = [15, 28, 32, 25]

    # Crear posiciones para las barras
    x = np.arange(len(categorias))  # [0, 1, 2, 3]
    # Definir el ancho de las barras
    width = 0.25  # Cada barra ocupará 0.25 unidades

    # Crear figura
    plt.figure(figsize=(12, 6))
    
    # Crear las barras
    # Cada conjunto de barras está desplazado por width
    plt.bar(x - width, valores1, width, label='Serie 1', color='#FF9999')
    plt.bar(x, valores2, width, label='Serie 2', color='#66B2FF')
    plt.bar(x + width, valores3, width, label='Serie 3', color='#99FF99')

    # Personalización
    plt.title('Gráfico de Barras Múltiple')
    plt.xlabel('Grupos')
    plt.ylabel('Valores')
    plt.xticks(x, categorias)  # Colocar las etiquetas en las posiciones correctas
    plt.legend()  # Mostrar leyenda
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.savefig('graficos/barras_multiple.png')
    plt.close()

def grafico_barras_apiladas():
    """Ejemplo de gráfico de barras apiladas"""
    # Datos
    categorias = ['Cat A', 'Cat B', 'Cat C', 'Cat D']
    valores1 = [10, 15, 12, 8]
    valores2 = [5, 7, 6, 9]
    valores3 = [8, 6, 9, 7]

    plt.figure(figsize=(10, 6))
    
    # Crear barras apiladas
    # bottom define dónde comienza cada barra
    plt.bar(categorias, valores1, label='Nivel 1', color='#FFB6C1')
    plt.bar(categorias, valores2, bottom=valores1, label='Nivel 2', color='#87CEEB')
    # Para el tercer nivel, sumamos los valores anteriores
    plt.bar(categorias, valores3, bottom=np.array(valores1) + np.array(valores2), 
            label='Nivel 3', color='#98FB98')

    plt.title('Gráfico de Barras Apiladas')
    plt.xlabel('Categorías')
    plt.ylabel('Valores Totales')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.savefig('graficos/barras_apiladas.png')
    plt.close()

def grafico_barras_horizontales():
    """Ejemplo de gráfico de barras horizontales"""
    # Datos
    categorias = ['Categoría 1', 'Categoría 2', 'Categoría 3', 'Categoría 4', 'Categoría 5']
    valores = [45, 32, 67, 89, 23]

    plt.figure(figsize=(10, 6))
    
    # Crear barras horizontales con barh
    # (similar a bar pero con orientación horizontal)
    bars = plt.barh(categorias, valores, color='lightcoral')
    
    # Añadir valores en las barras
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height()/2,
                f'{width}',
                ha='left', va='center', fontweight='bold')

    plt.title('Gráfico de Barras Horizontales')
    plt.xlabel('Valores')
    plt.ylabel('Categorías')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.savefig('graficos/barras_horizontales.png')
    plt.close()

def grafico_barras_personalizado():
    """Ejemplo de gráfico de barras altamente personalizado"""
    # Datos
    categorias = ['A', 'B', 'C', 'D', 'E']
    valores = [23, 45, 56, 78, 32]
    
    # Crear figura con fondo personalizado
    plt.figure(figsize=(12, 7), facecolor='#f0f0f0')
    
    # Crear barras con gradiente de color
    colors_list = ['#FF9999', '#FF7777', '#FF5555', '#FF3333', '#FF1111']
    
    # Crear las barras
    bars = plt.bar(categorias, valores, color=colors_list)
    
    # Añadir valor encima de cada barra
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height,
                f'{height}',
                ha='center', va='bottom', fontweight='bold')
    
    # Personalización avanzada
    plt.title('Gráfico de Barras Personalizado', fontsize=16, pad=20)
    plt.xlabel('Categorías', fontsize=12)
    plt.ylabel('Valores', fontsize=12)
    
    # Personalizar los ejes
    plt.gca().spines['top'].set_visible(False)  # Ocultar borde superior
    plt.gca().spines['right'].set_visible(False)  # Ocultar borde derecho
    
    # Agregar una cuadrícula solo para el eje Y
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Ajustar los márgenes
    plt.tight_layout()
    
    plt.savefig('graficos/barras_personalizado.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Función principal que ejecuta todos los ejemplos"""
    print("Generando gráficos de barras...")
    
    grafico_barras_simple()
    print("✓ Gráfico de barras simple generado")
    
    grafico_barras_multiple()
    print("✓ Gráfico de barras múltiple generado")
    
    grafico_barras_apiladas()
    print("✓ Gráfico de barras apiladas generado")
    
    grafico_barras_horizontales()
    print("✓ Gráfico de barras horizontales generado")
    
    grafico_barras_personalizado()
    print("✓ Gráfico de barras personalizado generado")
    
    print("\nTodos los gráficos han sido guardados en la carpeta 'graficos'")

if __name__ == "__main__":
    main()
