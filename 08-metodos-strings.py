# Métodos para strings

#En Python existen los siguientes métodos para strings:

#dir()
#Devuelve una lista de métodos y atributos de un objeto. Estos métodos y atributos se pueden usar en cualquier objeto de Python
#Por ejemplo:

pi = 3.14159
print("Métodos y atributos de pi:")
print(dir(pi))
print("--------------------------------")

texto = "Hola Mundo"
print("Métodos y atributos de texto:")
print(dir(texto))
print("--------------------------------")

lista = [1, 2, 3, 4, 5]
print("Métodos y atributos de lista:")
print(dir(lista))
print("--------------------------------")

#dir() devuelve una lista de métodos diferente para cada tipo de objeto

#1. len()
#Devuelve el número de caracteres de un string

ejemplo_1 = "aksjcbns<lkdc sduvhasdvcDC Xddddf"
cantidad_caracteres = len(ejemplo_1)
print("cantidad_caracteres: ", cantidad_caracteres)
print("--------------------------------")

#2. upper()
#Convierte un string a mayúsculas

ejemplo_2 = "Cualquier vaina"
mayusculas = ejemplo_2.upper()
print("mayusculas: ", mayusculas)
print("--------------------------------")

#3. lower()
#Convierte un string a minúsculas

ejemplo_3 = "AAAAAAAAAAAAAAAAAAAAAAAAH!!!"
minusculas = ejemplo_3.lower()
print("minusculas: ", minusculas)
print("--------------------------------")

#4. count()
#Devuelve el número de veces que aparece un substring en un string

ejemplo_4 = """
  El camino de la vida está lleno de sorpresas, de momentos de alegría y de tristeza. 
  Los recuerdos de la infancia son de color de rosa, llenos de sueños y de esperanzas.
"""
numero_veces = ejemplo_4.count("de")
print("numero_veces que aparece 'de': ", numero_veces)
print("--------------------------------")

#5. find()
#Devuelve el índice de la primera aparición de un substring en un string

ejemplo_5 = "Hola Mundo"
indice = ejemplo_5.find("Mundo")
print("indice: ", indice) #Devuelve el índice 5
print("--------------------------------")
#Si el substring no existe, find() devuelve -1

#6. replace()
#Reemplaza un substring por otro en un string

ejemplo_6 = """
  naturaleza viva
La naturaleza susurra entre los pinos,
La naturaleza danza al amanecer,
La naturaleza canta melodías de plata,
La naturaleza pinta el cielo al volar,
La naturaleza toca las nubes altas,
La naturaleza brilla con el sol nuevo,
La naturaleza florece sin cesar.
"""
reemplazo = ejemplo_6.replace("naturaleza", "chupaverga")
print("reemplazo: ", reemplazo)
print("--------------------------------")

#7. split()
#Convierte un string en una lista de strings

ejemplo_7 = "Hola Mundo"
lista = ejemplo_7.split() 
print("lista: ", lista) #['Hola', 'Mundo']
print("--------------------------------")

#8. index()
#Devuelve el índice de la primera aparición de un substring en un string

ejemplo_8 = "Hola Mundo"
indice = ejemplo_8.index("Mundo")
print("indice: ", indice) #Devuelve el índice 5
print("--------------------------------")
#La diferencia entre find() y index() es que index() devuelve un error si el substring no existe

#9. join()
#Convierte una lista de strings en un string

ejemplo_9 = ["Hola", "Mundo"]
string = " ".join(ejemplo_9)
print("string: ", string) #Devuelve "Hola Mundo"
print("--------------------------------")

#10. strip()
#Elimina los espacios en blanco al principio y al final de un string

ejemplo_10 = "   Hola Mundo   "
string = ejemplo_10.strip()
print("string: ", string) #Devuelve "Hola Mundo"
print("--------------------------------")

#11. isdigit()
#Devuelve True si el string es un número

ejemplo_11 = "12345"
print("ejemplo_11.isdigit(): ", ejemplo_11.isdigit()) #Devuelve True
print("--------------------------------")

#12. isalpha()
#Devuelve True si el string es alfabético

ejemplo_12 = "Hola Mundo"
print("ejemplo_12.isalpha(): ", ejemplo_12.isalpha()) #Devuelve True
print("--------------------------------")

#13. isspace()
#Devuelve True si el string es un espacio en blanco

ejemplo_13 = "         " #Asi de exagerado xD
print("ejemplo_13.isspace(): ", ejemplo_13.isspace()) #Devuelve True
print("--------------------------------")

#14. islower()
#Devuelve True si el string está en minúsculas

ejemplo_14 = "hola mundo"
print("ejemplo_14.islower(): ", ejemplo_14.islower()) #Devuelve True
print("--------------------------------")

#15. isupper()
#Devuelve True si el string está en mayúsculas

ejemplo_15 = "HOLA MUNDO"
print("ejemplo_15.isupper(): ", ejemplo_15.isupper()) #Devuelve True
print("--------------------------------")

#16. istitle()
#Devuelve True si el string está en formato de título

ejemplo_16 = "Hola Mundo Python"
print("ejemplo_16.istitle(): ", ejemplo_16.istitle()) #Devuelve True
print("--------------------------------")

#17. isalnum()
#Devuelve True si el string es alfanumérico

ejemplo_17 = "HolaMundoPython"
print("ejemplo_17.isalnum(): ", ejemplo_17.isalnum()) #Devuelve True
print("--------------------------------")


#Son un montón xD
