def ejemplo_division():
    try:
        # Intentamos dividir 10 entre 0
        resultado = 10 / 0
    except ZeroDivisionError: #esta directiva de "except" es lo que se va a ejecutar en caso de que el programa lance una excepción
        print("Error: No se puede dividir entre cero")
    else:
        print(f"El resultado es: {resultado}")
    finally: # El finally es raramente utilizado, aparentemente
        print("Esta parte siempre se ejecuta, haya o no excepción")

def ejemplo_archivo():
    try:
        # Intentamos abrir un archivo que no existe
        archivo = open("archivo_inexistente.txt", "r")
    except FileNotFoundError:
        print("Error: El archivo no existe")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    else:
        print("Archivo abierto correctamente")
        archivo.close()

def ejemplo_input():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            print(f"El número ingresado es: {numero}")
            break
        except ValueError:
            print("Error: Debe ingresar un número válido")

# Ejecutamos los ejemplos
if __name__ == "__main__":
    print("Ejemplo de división:")
    ejemplo_division()
    
    print("\nEjemplo de archivo:")
    ejemplo_archivo()
    
    print("\nEjemplo de input:")
    ejemplo_input()
