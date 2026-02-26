import bpy
import math

def limpiar_escena():
    # Es mejor separar la limpieza para no borrar accidentalmente lo que creas
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def crear_poligono_2d(nombre, lados, radio):
    # 1. Crear malla y objeto
    malla = bpy.data.meshes.new(nombre)
    objeto = bpy.data.objects.new(nombre, malla)
    bpy.context.collection.objects.link(objeto)
    
    vertices = []
    # Usamos una lista de índices para la cara (conecta del 0 al último)
    cara = [list(range(lados))] 
    
    # 2. Cálculo de vértices
    for i in range(lados):
        angulo = 2 * math.pi * i / lados
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        vertices.append((x, y, 0))
        
    # 3. Cargar datos (Vértices, Aristas vacío, Caras)
    # Al pasar la cara, Blender genera automáticamente las aristas
    malla.from_pydata(vertices, [], cara)
    malla.update()

# --- EJECUCIÓN ---
limpiar_escena()
crear_poligono_2d("Hexagono_Solid", lados=6, radio=5)

# Opcional: Centrar la vista en el nuevo objeto
bpy.ops.view3d.view_selected(use_all_regions=False)