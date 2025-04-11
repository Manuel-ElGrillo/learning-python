from math import pi

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return pi * (radio ** 2)

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def perimetro_circulo(radio):
    return 2 * pi * radio

__all__ = [
    'area_rectangulo', 
    'area_triangulo', 
    'area_circulo',
    'perimetro_rectangulo', 
    'perimetro_triangulo', 
    'perimetro_circulo'
]