# Las condiciones son un bloque de código que se ejecuta si una condición es verdadera.

# Ejemplo
texto = "Hola Mundo"

if texto == "Hola Mundo":
  print("El texto es idéntico")
else:
  print("El texto no es idéntico")

# También se puede usar el operador ternario
print("El texto es idéntico") if texto == "Hola Mundo" else print("El texto no es idéntico")

# También se puede usar el operador ternario para asignar un valor a una variable
texto2 = "Valor asignado" if texto == "Hola Mundo" else "El texto no es idéntico"
print("texto2: ", texto2)

########################################################################################

# Ejemplo de condicionales anidadas
ingresos = 5000
impuesto_1 = 3
impuesto_2 = 7

if ingresos == 5000:
  print(f"El usuario debe pagar un impuesto del {impuesto_1}%")
elif ingresos > 5000:
  print(f"El usuario debe pagar un impuesto del {impuesto_2}%")
else:
  print("El usuario no debe pagar impuestos")


