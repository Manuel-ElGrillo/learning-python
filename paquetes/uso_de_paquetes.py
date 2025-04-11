from calculos.aritmetica_basica import suma, resta, multiplica, divide, potencia, raiz_cuadrada
from calculos.geometria import area_rectangulo, area_triangulo, area_circulo, perimetro_rectangulo, perimetro_triangulo, perimetro_circulo
from calculos.estadistica import media, mediana, moda, varianza, desviacion_estandar

# Ejemplos de uso
if __name__ == "__main__": # __main__ es el archivo principal donde se ejecuta el programa
    # Aritmética básica
    print("Suma:", suma(5, 3))
    print("Potencia:", potencia(2, 3))
    
    # Geometría
    print("Área del círculo:", area_circulo(5))
    print("Perímetro del rectángulo:", perimetro_rectangulo(4, 6))
    
    # Estadística
    numeros = [1, 2, 2, 3, 4, 4, 4, 5]
    print("Media:", media(numeros))
    print("Mediana:", mediana(numeros))
    print("Moda:", moda(numeros))