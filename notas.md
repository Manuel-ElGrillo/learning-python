 - Python tiene su propia consola de comandos
 Se puede encontrar como un programa normal de Windows

 - Por razones de aprendizaje. EN cursor si empiezas o dejas comentarios reflejando una duda el autocompletado te permite resolverla sin necesidad de consultar al chat. :)

 To Do: hacer nota sobre lo hasheable

# Hash en Python

El hash es como un "DNI" o "identificador único" que Python usa para localizar objetos rápidamente en memoria. 

Puntos clave:
- Solo los objetos inmutables pueden tener hash
- Se usa principalmente en diccionarios (como claves) y sets
- Permite búsquedas muy rápidas O(1)

Reglas de oro:
1. Si es mutable → NO puede tener hash
2. Si tiene hash → DEBE ser inmutable
3. Si es inmutable → PODRÍA tener hash

Ejemplos:
- Hasheables: números, strings, tuplas (con elementos inmutables), frozensets
- No hasheables: listas, diccionarios, sets

Uso práctico:
- Diccionarios: las claves deben ser hasheables
- Sets: todos sus elementos deben ser hasheables
- Búsquedas rápidas: Python usa el hash como "dirección" para encontrar valores