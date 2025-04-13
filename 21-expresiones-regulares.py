import re

"""
Las expresiones regulares (regex) son patrones de búsqueda que nos permiten:
- Buscar texto que coincida con un patrón específico
- Validar formatos (como emails, números de teléfono, etc.)
- Extraer información de texto
- Reemplazar texto que coincida con un patrón

En Python, usamos el módulo 're' para trabajar con expresiones regulares.
"""

# Ejemplo 1: Búsqueda básica
texto = "Hola mundo, este es un ejemplo de expresiones regulares"
patron = "mundo"
resultado = re.search(patron, texto)
print(f"Ejemplo 1 - Búsqueda básica: {resultado.group() if resultado else 'No encontrado'}")

# Ejemplo 2: Validación de email
email = "usuario@ejemplo.com"
patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
es_valido = bool(re.match(patron_email, email))
print(f"Ejemplo 2 - Validación de email: {es_valido}")

# Ejemplo 3: Extracción de números
texto_numeros = "Tengo 3 manzanas y 5 naranjas"
numeros = re.findall(r'\d+', texto_numeros)
print(f"Ejemplo 3 - Números encontrados: {numeros}")

# Ejemplo 4: Reemplazo de texto
texto_original = "El gato es negro y el perro es blanco"
texto_modificado = re.sub(r'gato|perro', 'animal', texto_original)
print(f"Ejemplo 4 - Texto modificado: {texto_modificado}")

# Ejemplo 5: Validación de contraseña
# La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número
def validar_contraseña(contraseña):
    patron = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
    return bool(re.match(patron, contraseña))

contraseñas = ["Password123", "password", "PASS123", "pass123"]
print("\nEjemplo 5 - Validación de contraseñas:")
for pwd in contraseñas:
    print(f"{pwd}: {'Válida' if validar_contraseña(pwd) else 'Inválida'}")

# Ejemplo 6: Extracción de fechas
texto_fechas = "Las reuniones son el 15/03/2024 y el 20/04/2024"
fechas = re.findall(r'\d{2}/\d{2}/\d{4}', texto_fechas)
print(f"\nEjemplo 6 - Fechas encontradas: {fechas}")

# Ejemplo 7: División de texto
texto_para_dividir = "manzana,naranja,pera,plátano"
frutas = re.split(r',', texto_para_dividir)
print(f"\nEjemplo 7 - Frutas separadas: {frutas}")

"""
Explicación de algunos caracteres especiales en regex:
- ^ : Inicio de línea
- $ : Fin de línea
- . : Cualquier carácter
- * : 0 o más repeticiones
- + : 1 o más repeticiones
- ? : 0 o 1 repetición
- \d : Dígito
- \w : Carácter alfanumérico
- \s : Espacio en blanco
- [] : Conjunto de caracteres
- () : Grupo de captura
- | : devuelve un elemento o el otro
"""
