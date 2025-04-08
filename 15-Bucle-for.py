# Los bucles son una estructura de control que permite repetir un bloque de código un número determinado de veces.

# En Python existen dos tipos de bucles:
# 1. Bucle for
# 2. Bucle while

# De momento aquí solo se va a ver el for, lol

# Bucle for

# Sintaxis:
# for variable in range(inicio, fin, paso):
#     bloque de código

# Ejemplo:

for i in range(1, 11):
    print(i) # Imprime los números del 1 al 10

print("--------------------------------")

# Tipos de datos que se pueden iterar:
# - Strings
# - Listas
# - Tuplas
# - Diccionarios

# Ejemplo con strings:

for i in "Hola":
    print(i) # Imprime cada letra de la palabra "Hola"

print("--------------------------------")

# Ejemplo con listas:

for i in [1, 2, 3, 4, 5]:
    print(i) # Imprime cada elemento de la lista

print("--------------------------------")

# Ejemplo con tuplas:

for i in ("Hola", "Mundo", "Python"):
    print(i) # Imprime cada elemento de la tupla

print("--------------------------------")

# Ejemplo con diccionarios:

diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

for i in diccionario:
    print(i) # Imprime cada elemento del diccionario
    print(diccionario[i]) # Imprime el valor de cada elemento del diccionario

print("--------------------------------")

#Otra forma de iterar sobre un diccionario es usando el método items()

for i in diccionario.items():
    print(i) # Imprime cada elemento del diccionario como una tupla

print("--------------------------------")

# Ejemplo con sets / conjuntos:

for i in {1, 2, 3, 4, 5}:
    print(i) # Imprime cada elemento del set

print("--------------------------------")

# Los bucles en este lenguaje de programación tienen la particularidad de que se le puede colocar un else al final. Esto hace que se ejecute el bloque de código dentro del else una vez que se ha acabado el bucle SIEMPRE!!

for i in range(1, 11):
    print(i)
else:
    print("El bucle ha terminado")


# También se pueden usar las sentencias break y continue para determinar si el flujo del bucle debe continuar o no.

for i in range(1, 11):
    if i == 5:
        break # Sale del bucle
    print(i)

for i in range(1, 11):
    if i == 5:
        continue # Omite el número 5
    print(i)


