def media(numeros):
    if not numeros:
        return "Error: Lista vacía"
    return sum(numeros) / len(numeros)

def mediana(numeros):
    if not numeros:
        return "Error: Lista vacía"
    
    numeros_ordenados = sorted(numeros)
    longitud = len(numeros)
    
    if longitud % 2 == 0:
        # Si la longitud es par, promedio de los dos valores centrales
        medio1 = numeros_ordenados[longitud // 2 - 1]
        medio2 = numeros_ordenados[longitud // 2]
        return (medio1 + medio2) / 2
    else:
        # Si la longitud es impar, valor central
        return numeros_ordenados[longitud // 2]

def moda(numeros):
    if not numeros:
        return "Error: Lista vacía"
    
    # Crear diccionario de frecuencias
    frecuencias = {}
    for num in numeros:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    
    # Encontrar el valor más frecuente
    max_frecuencia = max(frecuencias.values())
    moda = [num for num, freq in frecuencias.items() if freq == max_frecuencia]
    
    return moda[0] if len(moda) == 1 else moda

def varianza(numeros):
    if not numeros:
        return "Error: Lista vacía"
    
    med = media(numeros)
    suma_cuadrados = sum((x - med) ** 2 for x in numeros)
    return suma_cuadrados / len(numeros)

def desviacion_estandar(numeros):
    if not numeros:
        return "Error: Lista vacía"
    
    return varianza(numeros) ** 0.5

__all__ = ['media', 'mediana', 'moda', 'varianza', 'desviacion_estandar']