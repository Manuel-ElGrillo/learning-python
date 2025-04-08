# Los datos compuestos son aquellos que contienen más de un valor.
# Los datos compuestos en Python son:
# - Listas
# - Tuplas
# - Conjuntos
# - Diccionarios


########################################################################################

# Ejemplo de lista:
# Con numeros
numeros = [1, 2, 3, 4, 5]
print(numeros)

# Con cadenas de texto
frutas = ["manzana", "naranja", "banana"]
print(frutas)

# Con diferentes tipos de datos
mezcla = [1, "manzana", True, 3.14]
print(mezcla)
print("Imprimiendo un elemento de la lista: ", mezcla[1])


########################################################################################

# Ejemplo de tupla:
# La diferencia entre una lista y una tupla es que la tupla es inmutable y su sintaxis es con parentesis () 
# Con numeros
punto = (3, 5)
print(punto)

# Es posible acceder a los elementos de la tupla por su indice
print("Imprimiendo un elemento de la tupla: ", punto[0])

# Con cadenas de texto
persona = ("Juan", "Perez", 30)
print(persona)

# Es posible acceder a los elementos de la tupla por su indice
print("Imprimiendo un elemento de la tupla: ", persona[0])


########################################################################################

# Ejemplo de conjunto:
# Los conjuntos son una colección de elementos únicos y no ordenados.
# La sintaxis es con llaves {}

conjunto = {1, 2, 3, 4, 5}
print(conjunto)

# Los conjuntos no admiten elementos duplicados
conjunto_duplicados = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(conjunto_duplicados)

# No es posible acceder a los elementos de el conjunto por su indice
# Los datos dentro de un conjunto no tienen un orden


########################################################################################

# Ejemplo de diccionario:
# Los diccionarios son una colección de elementos que se almacenan como pares clave-valor.
# Como si fuesen un objeto en JavaScript.
# La sintaxis es con llaves {}

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(diccionario)

# Es posible acceder a los elementos de el diccionario por su clave
print("Imprimiendo un elemento del diccionario: ", diccionario["nombre"])

#También existe una función para crear diccionarios y es la función dict()
diccionario = dict(nombre="Juan", edad=30, ciudad="Madrid")
print(diccionario)








