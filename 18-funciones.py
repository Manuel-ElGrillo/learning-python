# Funciones jujuuuuuuuuuuuuu

# Sintaxis

def nombre_funcion(parametros):
    # Cuerpo de la función
    return valor_de_retorno

# Ejecutando la función

nombre_funcion(parametros)

# Ejemplo

def saludar(nombre):
    return f"Hola, {nombre}!"

saludar("Grillo")

# Usando parámetros

def saludar(nombre, apellido):
    return f"Hola, {nombre} {apellido}!"

saludar("Grillo", "Garcia")


#Usando valores por defecto

def saludar(nombre, apellido="Garcia"):
    return f"Hola, {nombre} {apellido}!"

saludar("Grillo")

# Usando *args para recibir un número variable de argumentos

def sumar(*args):
    return sum(args)

sumar(1, 2, 3, 4, 5)

# Como nota adicional, *args es una tupla
# Y los *args se pueden usar en combinación con otros parámetros siempre y cuando este sea el último parámetro

def saludar(nombre, *args):
    return f"Hola, {nombre}! {args}"

saludar("Grillo", "Garcia", "Gomez")

# Usando **kwargs para recibir un número variable de argumentos nombrados
# PD: este es raro, no lo entendí del todo

def crear_persona(**kwargs):
    return f"Nombre: {kwargs['nombre']}, Apellido: {kwargs['apellido']}"

crear_persona(nombre="Grillo", apellido="Garcia")

