# Diferentes formas de importar módulos:

# 1. Importar todo el módulo
import operaciones_aritmeticas
resultado = operaciones_aritmeticas.suma(5, 3)

# 2. Importar funciones específicas
from operaciones_aritmeticas import suma, resta
resultado = suma(5, 3)
resultado_resta = resta(5, 3)
print(resultado_resta)

# 3. Importar todo con un alias
import operaciones_aritmeticas as op
resultado = op.suma(5, 3)

# 4. Importar todo (no recomendado)
from operaciones_aritmeticas import *
resultado = suma(5, 3)


# Importando las variables del otro módulo
from operaciones_aritmeticas import PI, E
print(PI)
print(E)


