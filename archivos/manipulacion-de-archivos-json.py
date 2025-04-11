# Manipulación de archivos JSON
# JSON es perfecto para configuraciones y datos estructurados

import json
from datetime import datetime
import os

# Definir la ruta de la carpeta archivos
RUTA_ARCHIVOS = os.path.dirname(__file__)

def crear_configuracion():
    print("Creando archivo de configuración JSON...")
    config = {
        "app_name": "Mi Aplicación",
        "version": "1.0.0",
        "fecha_actualizacion": datetime.now().strftime("%Y-%m-%d"),
        "configuraciones": {
            "tema": "oscuro",
            "idioma": "español",
            "notificaciones": True
        },
        "usuarios_permitidos": [
            {"id": 1, "nombre": "José Martínez", "permisos": "total"},
            {"id": 2, "nombre": "María Rodríguez", "permisos": "lectura"}
        ]
    }
    
    ruta_config = os.path.join(RUTA_ARCHIVOS, 'config.json')
    with open(ruta_config, 'w', encoding='utf-8') as archivo:
        json.dump(config, archivo, indent=4, ensure_ascii=False)

def actualizar_configuracion(clave, valor):
    ruta_config = os.path.join(RUTA_ARCHIVOS, 'config.json')
    with open(ruta_config, 'r', encoding='utf-8') as archivo:
        config = json.load(archivo)
    
    config["configuraciones"][clave] = valor
    
    with open(ruta_config, 'w', encoding='utf-8') as archivo:
        json.dump(config, archivo, indent=4, ensure_ascii=False)

def crear_base_datos():
    print("\nCreando base de datos JSON...")
    base_datos = {
        "productos": [
            {
                "id": 1,
                "nombre": "Portátil",
                "descripción": "Última generación",
                "precio": 999.99,
                "stock": 50
            },
            {
                "id": 2,
                "nombre": "Teléfono móvil",
                "descripción": "Cámara de última generación",
                "precio": 499.99,
                "stock": 100
            }
        ],
        "metadata": {
            "ultima_actualizacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_productos": 2
        }
    }
    
    ruta_db = os.path.join(RUTA_ARCHIVOS, 'database.json')
    with open(ruta_db, 'w', encoding='utf-8') as archivo:
        json.dump(base_datos, archivo, indent=4, ensure_ascii=False)

def agregar_producto(nombre, descripcion, precio, stock):
    ruta_db = os.path.join(RUTA_ARCHIVOS, 'database.json')
    with open(ruta_db, 'r', encoding='utf-8') as archivo:
        base_datos = json.load(archivo)
    
    nuevo_id = max(p["id"] for p in base_datos["productos"]) + 1
    
    nuevo_producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "descripción": descripcion,
        "precio": precio,
        "stock": stock
    }
    
    base_datos["productos"].append(nuevo_producto)
    base_datos["metadata"]["total_productos"] += 1
    base_datos["metadata"]["ultima_actualizacion"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(ruta_db, 'w', encoding='utf-8') as archivo:
        json.dump(base_datos, archivo, indent=4, ensure_ascii=False)

# Ejecutar ejemplos
if __name__ == "__main__":
    # Crear y manipular configuración
    crear_configuracion()
    actualizar_configuracion("tema", "claro")
    
    print("\nLeyendo configuración:")
    ruta_config = os.path.join(RUTA_ARCHIVOS, 'config.json')
    with open(ruta_config, 'r', encoding='utf-8') as archivo:
        config = json.load(archivo)
        print(json.dumps(config, indent=2, ensure_ascii=False))
    
    # Crear y manipular base de datos
    crear_base_datos()
    agregar_producto(
        "Tableta gráfica", 
        "Perfecta para diseñadores", 
        299.99, 
        75
    )
    
    print("\nLeyendo base de datos:")
    ruta_db = os.path.join(RUTA_ARCHIVOS, 'database.json')
    with open(ruta_db, 'r', encoding='utf-8') as archivo:
        base_datos = json.load(archivo)
        print(json.dumps(base_datos, indent=2, ensure_ascii=False))