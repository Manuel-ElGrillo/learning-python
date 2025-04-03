#Ejercicio 1
#Hay que determinar:
# A) Diferencia en porcentaje entre el curso actual y:
#  - EL más rápido de otros cursos
#  - EL más lento de otros cursos
#  - El promedio de otros cursos

# Datos: 
duracion_curso_actual = 8.0
duracion_curso_mas_rapido = 1.5
duracion_curso_mas_lento = 7.0
promedio_duracion_cursos = (duracion_curso_mas_rapido + duracion_curso_mas_lento) / 2

print(f"El promedio de duracion de los cursos es: {promedio_duracion_cursos} horas")

diferencia_porcentaje_curso_actual = (duracion_curso_actual - promedio_duracion_cursos) / promedio_duracion_cursos * 100

print(f"La diferencia en porcentaje entre el curso actual y el promedio de los otros cursos es: {diferencia_porcentaje_curso_actual.__round__(2)} %")

#NOTA: El tipo se complica con formulas que son algo trickys de entender