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

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    if numero >= 0:
        return numero ** 0.5
    return "Error: Número negativo"

__all__ = ['suma', 'resta', 'multiplica', 'divide', 'potencia', 'raiz_cuadrada']