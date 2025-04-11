# Manipulación de archivos CSV
# Los CSV son excelentes para datos tabulares y hojas de cálculo

import csv
from datetime import datetime
import os

# Definir la ruta de la carpeta archivos
RUTA_ARCHIVOS = os.path.dirname(__file__)

def crear_lista_estudiantes():
    print("Creando archivo CSV de estudiantes...")
    estudiantes = [
        ['ID', 'Nombre', 'Edad', 'Promedio'],
        [1, 'Ana García', 20, 9.5],
        [2, 'Juan Pérez', 22, 8.7],
        [3, 'María López', 21, 9.2]
    ]
    
    ruta_estudiantes = os.path.join(RUTA_ARCHIVOS, 'estudiantes.csv')
    with open(ruta_estudiantes, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerows(estudiantes)

def agregar_estudiante(id, nombre, edad, promedio):
    ruta_estudiantes = os.path.join(RUTA_ARCHIVOS, 'estudiantes.csv')
    with open(ruta_estudiantes, 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([id, nombre, edad, promedio])

def leer_estudiantes():
    estudiantes = []
    ruta_estudiantes = os.path.join(RUTA_ARCHIVOS, 'estudiantes.csv')
    with open(ruta_estudiantes, 'r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            estudiantes.append(row)
    return estudiantes

def crear_calificaciones():
    print("\nCreando archivo CSV de calificaciones...")
    calificaciones = [
        {'Estudiante': 'Ana García', 'Materia': 'Python', 'Calificación': 95},
        {'Estudiante': 'Juan Pérez', 'Materia': 'Python', 'Calificación': 87},
        {'Estudiante': 'María López', 'Materia': 'Python', 'Calificación': 92}
    ]
    
    ruta_calificaciones = os.path.join(RUTA_ARCHIVOS, 'calificaciones.csv')
    with open(ruta_calificaciones, 'w', newline='', encoding='utf-8') as archivo:
        campos = ['Estudiante', 'Materia', 'Calificación']
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(calificaciones)

def leer_calificaciones():
    calificaciones = []
    ruta_calificaciones = os.path.join(RUTA_ARCHIVOS, 'calificaciones.csv')
    with open(ruta_calificaciones, 'r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            calificaciones.append(row)
    return calificaciones

# Ejecutar ejemplos
if __name__ == "__main__":
    # Crear y manipular lista de estudiantes
    crear_lista_estudiantes()
    agregar_estudiante(4, 'Pedro Sánchez', 23, 8.9)
    
    print("\nLeyendo estudiantes:")
    estudiantes = leer_estudiantes()
    for estudiante in estudiantes:
        print(estudiante)
    
    # Crear y leer calificaciones
    crear_calificaciones()
    
    print("\nLeyendo calificaciones:")
    calificaciones = leer_calificaciones()
    for calif in calificaciones:
        print(f"Estudiante: {calif['Estudiante']}, "
              f"Calificación: {calif['Calificación']}")