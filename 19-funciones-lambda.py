# Funciones Lambda en Python
# También conocidas como funciones anónimas
# Sintaxis: lambda argumentos: expresión

#################################################################
# Sintaxis Básica
#################################################################

# Función normal vs Lambda
def cuadrado(x):
    return x ** 2

# La misma función como lambda
cuadrado_lambda = lambda x: x ** 2

print("Normal:", cuadrado(5))      # Normal: 25
print("Lambda:", cuadrado_lambda(5))  # Lambda: 25

#################################################################
# Casos de Uso Comunes
#################################################################

# 1. Funciones de una sola línea
suma = lambda a, b: a + b
print("Suma:", suma(5, 3))  # Suma: 8

# 2. Funciones dentro de funciones
def multiplicador(n):
    return lambda x: x * n

duplicar = multiplicador(2)
triplicar = multiplicador(3)

print("Duplicar 5:", duplicar(5))    # Duplicar 5: 10
print("Triplicar 5:", triplicar(5))  # Triplicar 5: 15

# 3. Con map() - Aplicar función a cada elemento
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)  # Cuadrados: [1, 4, 9, 16, 25]

# 4. Con filter() - Filtrar elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)  # Números pares: [2, 4]

# 5. Con sorted() - Ordenar con función personalizada
estudiantes = [
    {'nombre': 'Ana', 'nota': 90},
    {'nombre': 'Juan', 'nota': 85},
    {'nombre': 'María', 'nota': 95}
]

ordenados = sorted(estudiantes, key=lambda x: x['nota'], reverse=True)
print("Estudiantes ordenados por nota:", ordenados)

#################################################################
# Ejemplos Prácticos
#################################################################

# 1. Operaciones matemáticas
operaciones = {
    'suma': lambda a, b: a + b,
    'resta': lambda a, b: a - b,
    'multiplica': lambda a, b: a * b,
    'divide': lambda a, b: a / b if b != 0 else "Error: División por cero"
}

print("Suma:", operaciones['suma'](10, 5))        # 15
print("Resta:", operaciones['resta'](10, 5))      # 5
print("Multiplica:", operaciones['multiplica'](10, 5))  # 50
print("Divide:", operaciones['divide'](10, 5))    # 2.0

# 2. Procesamiento de texto
textos = ['python', 'JavaScript', 'JAVA', 'PHP']
# Convertir a mayúsculas
mayusculas = list(map(lambda x: x.upper(), textos))
# Longitud de cada texto
longitudes = list(map(lambda x: len(x), textos))

print("Mayúsculas:", mayusculas)
print("Longitudes:", longitudes)

# 3. Filtrado condicional
datos = [
    {'nombre': 'Juan', 'edad': 25, 'activo': True},
    {'nombre': 'Ana', 'edad': 17, 'activo': False},
    {'nombre': 'María', 'edad': 30, 'activo': True}
]

# Filtrar mayores de edad activos
activos_mayores = list(filter(
    lambda x: x['edad'] >= 18 and x['activo'], 
    datos
))
print("Activos mayores de edad:", activos_mayores)

#################################################################
# Ventajas y Desventajas
#################################################################

# Ventajas:
# 1. Código más conciso para funciones simples
# 2. Útil para funciones de un solo uso
# 3. Más legible en funciones como map(), filter(), sorted()
# 4. No necesita un nombre (función anónima)

# Desventajas:
# 1. Solo puede contener una expresión
# 2. Menos legible para operaciones complejas
# 3. No puede contener múltiples líneas de código
# 4. No puede contener declaraciones (if, for, while, etc.)

#################################################################
# Buenas Prácticas
#################################################################

# 1. Usar lambda para operaciones simples y cortas
# 2. Preferir funciones normales para lógica compleja
# 3. Usar nombres descriptivos cuando se asigna a una variable
# 4. No abusar de las lambdas - mantener el código legible

# Ejemplo de buen uso:
ordenar_por_edad = lambda x: x['edad']
datos_ordenados = sorted(datos, key=ordenar_por_edad)

# Ejemplo de mal uso (mejor usar función normal):
# complejo = lambda x: [i for i in range(x) if i % 2 == 0 and i > 5]
