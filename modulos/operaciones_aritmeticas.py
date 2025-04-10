# Módulos en Python
# Un módulo es un archivo .py que contiene código Python reutilizable

# 1. Definimos algunas funciones básicas de aritmética
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Error: División por cero"

# 2. Variables que queremos compartir
PI = 3.14159
E = 2.71828

# 3. Podemos definir qué queremos exponer cuando alguien importe este módulo
__all__ = ['suma', 'resta', 'multiplica', 'divide', 'PI', 'E']
# __all__ es una variable que define qué funciones y variables se van a importar cuando alguien importe este módulo. Lo que está dentro de la lista es lo que se va a importar.

# 4. Código que se ejecuta solo si este archivo es el principal
if __name__ == "__main__":
    # Este código solo se ejecuta si ejecutamos este archivo directamente
    print("Probando operaciones:")
    print(f"Suma: {suma(5, 3)}")
    print(f"Resta: {resta(5, 3)}")
    print(f"Multiplicación: {multiplica(5, 3)}")
    print(f"División: {divide(5, 3)}")
