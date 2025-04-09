# Funciones Nativas (Built-in) de Python
# Esta es una guía completa de las funciones más importantes incorporadas en Python

#################################################################
# Funciones de Conversión de Tipos
#################################################################

# int(): Convierte a número entero
entero = int("123")  # 123
entero_float = int(3.14)  # 3

# float(): Convierte a número decimal
decimal = float("3.14")  # 3.14
decimal_entero = float(3)  # 3.0

# str(): Convierte a string/texto
texto = str(123)  # "123"
texto_bool = str(True)  # "True"

# bool(): Convierte a booleano
booleano = bool(1)  # True
booleano_vacio = bool("")  # False

# list(): Convierte a lista
lista = list("Hola")  # ['H', 'o', 'l', 'a']
lista_tupla = list((1, 2, 3))  # [1, 2, 3]

# tuple(): Convierte a tupla
tupla = tuple([1, 2, 3])  # (1, 2, 3)

# set(): Convierte a conjunto
conjunto = set([1, 2, 2, 3])  # {1, 2, 3}

# dict(): Convierte a diccionario
diccionario = dict(nombre="Juan", edad=25)  # {"nombre": "Juan", "edad": 25}

#################################################################
# Funciones Matemáticas
#################################################################

# abs(): Valor absoluto
absoluto = abs(-5)  # 5

# round(): Redondea un número
redondeado = round(3.7)  # 4
redondeado_decimales = round(3.14159, 2)  # 3.14

# max(): Valor más alto
maximo = max(1, 2, 3)  # 3
maximo_lista = max([1, 2, 3])  # 3

# min(): Valor más bajo
minimo = min(1, 2, 3)  # 1

# sum(): Suma todos los elementos
suma = sum([1, 2, 3])  # 6

# pow(): Potencia
potencia = pow(2, 3)  # 8 (2³)

#################################################################
# Funciones de Secuencias
#################################################################

# len(): Longitud
longitud = len("Hola")  # 4
longitud_lista = len([1, 2, 3])  # 3

# range(): Genera secuencia
numeros = list(range(3))  # [0, 1, 2]
numeros_paso = list(range(0, 10, 2))  # [0, 2, 4, 6, 8]

# enumerate(): Índice y valor
for i, letra in enumerate(['a', 'b', 'c']):
    print(f"Índice {i}: {letra}")

# zip(): Combina iterables
nombres = ["Juan", "Ana"]
edades = [25, 30]
combinado = list(zip(nombres, edades))  # [("Juan", 25), ("Ana", 30)]

# sorted(): Ordena
ordenado = sorted([3, 1, 2])  # [1, 2, 3]
ordenado_reversa = sorted([3, 1, 2], reverse=True)  # [3, 2, 1]

#################################################################
# Funciones de Inspección
#################################################################

# type(): Tipo de objeto
tipo = type(123)  # <class 'int'>
tipo_texto = type("Hola")  # <class 'str'>

# isinstance(): Verifica tipo
es_entero = isinstance(123, int)  # True
es_string = isinstance(123, str)  # False

# dir(): Lista atributos
atributos = dir("")  # Lista todos los métodos de string

# id(): Identificador único
id_objeto = id("Hola")  # número único

#################################################################
# Funciones de Input/Output
#################################################################

# print(): Imprime
print("Hola", "Mundo")  # Hola Mundo
print("Hola", end="!")  # Hola!

# format(): Formatea strings
mensaje = "Hola {}".format("Mundo")  # "Hola Mundo"
mensaje_multiple = "{} tiene {} años".format("Juan", 25)

#################################################################
# Funciones de Iteración
#################################################################

# map(): Aplica función a cada elemento
numeros = [1, 2, 3]
cuadrados = list(map(lambda x: x**2, numeros))  # [1, 4, 9]

# filter(): Filtra elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))  # [2]

# any(): True si alguno es True
hay_positivo = any([False, False, True])  # True

# all(): True si todos son True
todos_positivos = all([True, True, True])  # True

#################################################################
# Ejemplos de Uso Práctico
#################################################################

def ejemplo_practico():
    # Convertir input a número
    # numero = int(input("Ingresa un número: "))
    
    # Crear lista de números
    numeros = list(range(1, 6))  # [1, 2, 3, 4, 5]
    
    # Obtener cuadrados
    cuadrados = list(map(lambda x: x**2, numeros))
    
    # Filtrar pares
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    
    # Combinar nombres y edades
    nombres = ["Ana", "Juan"]
    edades = [25, 30]
    personas = dict(zip(nombres, edades))
    
    return numeros, cuadrados, pares, personas

# Ejecutar ejemplo
numeros, cuadrados, pares, personas = ejemplo_practico()
print("Números:", numeros)
print("Cuadrados:", cuadrados)
print("Pares:", pares)
print("Personas:", personas)

#################################################################
# Notas Importantes:
# 1. Todas estas funciones están disponibles sin necesidad de importar
# 2. Son la base del lenguaje y se usan constantemente
# 3. Algunas funciones pueden usarse como constructores
# 4. La mayoría son muy eficientes por estar implementadas en C
#################################################################
