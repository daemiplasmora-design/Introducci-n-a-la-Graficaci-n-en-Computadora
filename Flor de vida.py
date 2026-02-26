import bpy
import math

# Limpiar escena
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

# Parámetros de la figura
radio = 3
segmentos = 64
paso_angular = 60  # Para obtener 6 círculos alrededor
angulo_actual = 0
contador = 0

# 1. Círculo central
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0, 0, 0), vertices=segmentos)

# 2. Ciclo while para los círculos exteriores
while contador < 6:
    # Cálculo de posición
    x = radio * math.cos(math.radians(angulo_actual))
    y = radio * math.sin(math.radians(angulo_actual))
    
    # Crear círculo
    bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x, y, 0), vertices=segmentos)
    
    # Actualización de variables para la siguiente vuelta
    angulo_actual += paso_angular  # Sumamos 60 grados
    contador += 1                  # Incrementamos el contador