# Metodos para listas

# Mostrando con dir() los diferentes métodos que existen para una lista:
lista_random = ["Cualquier vaina", 1, True, 3.14]

metodos_de_listas = dir(lista_random)

print(metodos_de_listas)
print("--------------------------------")
print(" ")

# Métodos de listas

# append()
# Añade un elemento al final de la lista

lista_1 = [1,2,3,4,5]
lista_1.append(6)
print(lista_1)
print(" ")

# pop()
# Elimina el último elemento de la lista

lista_2 = [1,2,3,4,5]
lista_2.pop()
print("pop: ", lista_2)
print(" ")
# Si coloco -1 en el parámetro de pop(), elimina el último elemento de la lista
lista_2.pop(-1)
print("pop(-1): ", lista_2) # -2 si es el penúltimo elemento y así :) Tambieén sirve colocando números positivos
print(" ")

# remove()
# Elimina el primer elemento de la lista que coincide con el valor especificado

lista_3 = [1,2,3,4,5]
lista_3.remove(3)
print(lista_3)
print(" ")

# extend()
# Añade los elementos de una lista al final de otra lista

lista_4 = [1,2,3,4,5]
lista_4.extend([6,7,8,9,10])
print(lista_4)
print(" ")

#index()
# Devuelve el índice del primer elemento de la lista que coincide con el valor especificado

lista_5 = [1,2,3,4,5]
print(lista_5.index(3))
print(" ")
#devuelve 2 porque el 3 está en el índice 2

#insert()
# Inserta un elemento en la posición especificada

lista_6 = [1,2,3,4,5]
lista_6.insert(2, "Cuadrando este string in extremis a la lista, saludos")
print(lista_6)
print(" ")
# clear()
# Elimina todos los elementos de la lista

lista_7 = [1,2,3,4,5]
lista_7.clear()
print(lista_7)
print(" ")

# count()
# Devuelve el número de veces que aparece un elemento en la lista

lista_8 = [1,2,3,4,5,1,2,3,4,5]
print(lista_8.count(1))
print(" ")

# sort()
# Ordena los elementos de la lista de forma ascendente

lista_9 = [5,4,3,2,1]
lista_9.sort()
print(lista_9)
print(" ")

# reverse()
# Invierte el orden de los elementos de la lista

lista_10 = [1,2,3,4,5]
lista_10.reverse()
print(lista_10)
print(" ")
# Si fuesen strings, se invertiría el orden de los caracteres

lista_11 = ["Hola", "Mundo", "Python"]
lista_11.reverse()
print(lista_11)
print(" ")

# copy()
# Devuelve una copia de la lista

lista_12 = [1,2,3,4,5]
lista_12.copy()
print(lista_12)
print(" ")

#Esta copia es una referencia a la lista original, por lo que si se modifica la copia, se modifica la lista original
lista_13 = [1,2,3,4,5]
lista_13_copia = lista_13.copy()
lista_13_copia.append(6)
print(lista_13)
print(lista_13_copia)
print(" ")

#len()
# Devuelve el número de elementos de la lista

lista_14 = [1,2,3,4,5]
print(len(lista_14))  
print(" ")

#max()
# Devuelve el elemento más grande de la lista

lista_15 = [1,2000,3,4,5,100]
print(max(lista_15))
print(" ")

#min()
# Devuelve el elemento más pequeño de la lista  

lista_16 = [1,2,3,4,5]
print(min(lista_16))
print(" ")

#sum()
# Devuelve la suma de los elementos de la lista

lista_17 = [1,2,3,4,5]
print(sum(lista_17))
print(" ")

#any()
# Devuelve True si al menos un elemento de la lista es True

lista_18 = [True, False, True]
print(any(lista_18))
print(" ")

#all()
# Devuelve True si todos los elementos de la lista son True

lista_19 = [True, True, True]
print(all(lista_19))
print(" ")
# Se pueden considerar elementos truthy como 1, "Hola", True, etc.
# y falsys como 0, "", False, None, etc.
