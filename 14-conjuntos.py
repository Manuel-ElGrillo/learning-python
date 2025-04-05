# Conjuntos en Python

#Los conjuntos se pueden crear con la función set()

conjunto = set([1, 2, 3, 4, 5])

#Los conjuntos no admiten elementos duplicados

print("Conjunto original:", conjunto)

#Los conjuntos no tienen un orden

#print(conjunto[0]) #Esto dará un error

#Los conjuntos sirven para almacenar datos que no se repiten


##########################################


#Teoría de Conjuntos

#Los conjuntos se pueden usar para representar teoría de conjuntos

#Ejemplo:

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

#Unión de conjuntos (A U B)

union = conjunto_a | conjunto_b

print("Unión de conjuntos:", union)

#Intersección de conjuntos (A ∩ B)
#la intersección de conjuntos es el conjunto de elementos que están en ambos conjuntos

interseccion = conjunto_a & conjunto_b

print("Intersección de conjuntos:", interseccion)

#Diferencia de conjuntos (A - B)
#la diferencia de conjuntos es el conjunto de elementos que están en el primer conjunto y no en el segundo

diferencia = conjunto_a - conjunto_b

print("Diferencia de conjuntos:", diferencia)

#Diferencia simétrica de conjuntos (A Δ B)
#la diferencia simétrica de conjuntos es el conjunto de elementos que están en uno de los conjuntos y no en ambos

diferencia_simetrica = conjunto_a ^ conjunto_b

print("Diferencia simétrica de conjuntos:", diferencia_simetrica)

#Complemento de un conjunto (A')
#el complemento de un conjunto es el conjunto de elementos que están en el universo y no en el conjunto

universo = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

complemento = universo - conjunto_a

print("Complemento de un conjunto:", complemento)


#Subconjuntos y superconjuntos

#Un conjunto A es subconjunto de B si todos los elementos de A están en B

subconjunto = {1, 2, 3}
superset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("Subconjunto:", subconjunto.issubset(superset))

#Un conjunto A es superconjunto de B si todos los elementos de B están en A

print("Superconjunto:", superset.issuperset(subconjunto))

#Conjuntos disjuntos

#Dos conjuntos son disjuntos si no tienen elementos en común

conjunto_c = {1, 2, 3}
conjunto_d = {4, 5, 6}

print("Conjuntos disjuntos:", conjunto_c.isdisjoint(conjunto_d))

#Cardinalidad de un conjunto

#La cardinalidad de un conjunto es el número de elementos que tiene el conjunto

print("Cardinalidad de un conjunto:", len(conjunto_a))

#Producto cartesiano de dos conjuntos

#WIP











