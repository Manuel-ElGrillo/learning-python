# Manipulación de archivos TXT
# Los archivos TXT son perfectos para logs, notas, y texto simple

from datetime import datetime
import os

# Definir la ruta de la carpeta archivos
RUTA_ARCHIVOS = os.path.dirname(__file__)  # Obtiene la ruta del directorio actual

def crear_nota():
    print("Creando archivo de notas...")
    ruta_notas = os.path.join(RUTA_ARCHIVOS, 'notas.txt')
    with open(ruta_notas, 'w', encoding='utf-8') as archivo:
        archivo.write("=== Mis Notas Personales ===\n")
        archivo.write("Creado: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
        archivo.write("1. Aprender Python\n")
        archivo.write("2. Practicar con archivos\n")
        archivo.write("3. Hacer ejercicios\n")

def agregar_nota(nota):
    ruta_notas = os.path.join(RUTA_ARCHIVOS, 'notas.txt')
    with open(ruta_notas, 'a', encoding='utf-8') as archivo:
        archivo.write(f"{len(get_notas()) + 1}. {nota}\n")

def get_notas():
    ruta_notas = os.path.join(RUTA_ARCHIVOS, 'notas.txt')
    with open(ruta_notas, 'r', encoding='utf-8') as archivo:
        return [linea.strip() for linea in archivo if linea.strip().startswith(tuple('123456789'))]

def crear_log():
    print("\nCreando archivo de registro...")
    ruta_registro = os.path.join(RUTA_ARCHIVOS, 'registro.txt')
    with open(ruta_registro, 'w', encoding='utf-8') as archivo:
        archivo.write(f"=== Log de Actividades ===\n")
        archivo.write(f"Inicio de registro: {datetime.now()}\n")

def registrar_actividad(actividad):
    ruta_registro = os.path.join(RUTA_ARCHIVOS, 'registro.txt')
    with open(ruta_registro, 'a', encoding='utf-8') as archivo:
        archivo.write(f"{datetime.now().strftime('%H:%M:%S')} - {actividad}\n")

# Ejecutar ejemplos
if __name__ == "__main__":
    # Crear y manipular notas
    crear_nota()
    agregar_nota("Repasar funciones")
    agregar_nota("Hacer proyecto final")
    agregar_nota("Práctica con acentos y ñ")  # Prueba de caracteres especiales
    
    print("\nLeyendo notas:")
    ruta_notas = os.path.join(RUTA_ARCHIVOS, 'notas.txt')
    with open(ruta_notas, 'r', encoding='utf-8') as archivo:
        print(archivo.read())
    
    # Crear y manipular log
    crear_log()
    registrar_actividad("Inicio del programa")
    registrar_actividad("Creación de notas")
    registrar_actividad("Actualización de registros")
    registrar_actividad("Añadiendo entrada con ñ y tildes")  # Prueba de caracteres especiales
    
    print("\nLeyendo registro:")
    ruta_registro = os.path.join(RUTA_ARCHIVOS, 'registro.txt')
    with open(ruta_registro, 'r', encoding='utf-8') as archivo:
        print(archivo.read())
