# Metodos para diccionarios

ejemplo_diccionario = {
    "nombre": "Juan",
    "edad": 20,
    "ciudad": "Madrid"
}

metodos_disponibles = dir(ejemplo_diccionario)
print("Métodos disponibles para diccionarios: ", metodos_disponibles)
print(" ")

# Keys()
# Devuelve una lista de las claves del diccionario

print(ejemplo_diccionario.keys()) #nombre, edad, ciudad
print(" ")

# Values()
# Devuelve una lista de los valores del diccionario

print(ejemplo_diccionario.values()) #Juan, 20, Madrid
print(" ")

# Items()
# Devuelve una lista de tuplas (clave, valor) del diccionario

print(ejemplo_diccionario.items()) #('nombre', 'Juan'), ('edad', 20), ('ciudad', 'Madrid')
print(" ")

# get()
# Devuelve el valor de la clave especificada

print(ejemplo_diccionario.get("nombre")) #Juan
print(" ")

# pop()
# Elimina el elemento con la clave especificada y devuelve su valor

print(ejemplo_diccionario.pop("edad")) #20
print(" ")

# popitem()
# Elimina el último elemento del diccionario y devuelve una tupla (clave, valor)

print(ejemplo_diccionario.popitem()) #('ciudad', 'Madrid')
print(" ")

# clear()
# Elimina todos los elementos del diccionario

ejemplo_diccionario.clear()
print(ejemplo_diccionario) #{}
print(" ")

# copy()
# Devuelve una copia del diccionario

ejemplo_diccionario_copia = ejemplo_diccionario.copy()
print(ejemplo_diccionario_copia) #{'nombre': 'Juan', 'edad': 20, 'ciudad': 'Madrid'}
print(" ")

# fromkeys()
# Crea un nuevo diccionario con las claves especificadas y un valor por defecto

ejemplo_diccionario_fromkeys = {}.fromkeys(["nombre", "edad", "ciudad"], "valor_por_defecto")
print(ejemplo_diccionario_fromkeys) #{'nombre': 'valor_por_defecto', 'edad': 'valor_por_defecto', 'ciudad': 'valor_por_defecto'}
print(" ")

# setdefault()
# Devuelve el valor de la clave especificada, si no existe, lo agrega y devuelve el valor por defecto

print(ejemplo_diccionario.setdefault("nombre", "valor_por_defecto")) #Juan
print(" ")






