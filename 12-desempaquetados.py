# Desempaquetado en Python
# Es una característica que permite asignar elementos de una secuencia (lista, tupla) a variables individuales

# Ejemplo básico de desempaquetado
numeros = [1, 2, 3]
x, y, z = numeros  # Desempaquetado
print(f"x: {x}, y: {y}, z: {z}")

# Desempaquetado con strings
nombre_completo = ["Juan", "Pedro", "García"]
nombre, segundo_nombre, apellido = nombre_completo
print(f"Nombre completo: {nombre} {segundo_nombre} {apellido}")

# Usando * para capturar múltiples elementos
# El * permite capturar varios elementos en una lista
primero, *resto = [1, 2, 3, 4, 5]
print(f"Primer número: {primero}")
print(f"Resto de números: {resto}")

# Desempaquetado ignorando valores con _
nombre, _, apellido = ["María", "Isabel", "López"]
print(f"Nombre y apellido: {nombre} {apellido}")  # Ignoramos el segundo nombre

# Desempaquetado de tuplas
coordenadas = (10, 20)
x, y = coordenadas
print(f"Coordenada X: {x}, Coordenada Y: {y}")

# Intercambio de variables usando desempaquetado
a = 5
b = 10
a, b = b, a  # Intercambio de valores
print(f"a: {a}, b: {b}")
