# Unidad I: Introducción a la Graficación por Computadora

Esta unidad sienta las bases teóricas y matemáticas para la representación visual mediante sistemas digitales.

## 1.1 Historia y evolución de la graficación por computadora

La graficación ha pasado de ser una herramienta experimental a la base de la interfaz humano-computadora moderna:

* **Inicios (1950-1960):** Uso de tubos de rayos catódicos (CRT) y el surgimiento de **Sketchpad** de Ivan Sutherland, que introdujo el concepto de estructuras de datos jerárquicas para objetos gráficos.
* **Era del Renderizado (1970-1980):** Desarrollo de algoritmos fundamentales como el sombreado de Gouraud y Phong, y el nacimiento del **Ray Tracing**.
* **Modernidad:** Integración de GPUs dedicadas, trazado de rayos en tiempo real y generación procedural basada en inteligencia artificial.

## 1.2 Áreas de aplicación

La graficación impacta diversas disciplinas de la ingeniería y la ciencia:

* **CAD/CAM (Diseño y Fabricación Asistida):** Esencial en la ingeniería civil y mecánica para el prototipado de piezas y estructuras.
* **Visualización Científica y Médica:** Representación de fenómenos físicos complejos o datos de tomografías computarizadas.
* **Simulación y Entrenamiento:** Entornos virtuales para capacitación militar, aeronáutica o médica.
* **Entretenimiento:** Desarrollo de videojuegos y efectos visuales (VFX) en el cine.

## 1.3 Aspectos matemáticos de la graficación

La graficación es, esencialmente, geometría aplicada. Los conceptos clave incluyen:

* **Espacios de Coordenadas:** Comprensión de coordenadas locales, de mundo y de cámara.
* 
**Vectores y Matrices:** Uso de álgebra lineal para realizar transformaciones tridimensionales.


* **Coordenadas Homogéneas:** Permiten unificar las traslaciones y rotaciones en matrices de $4 \times 4$.

## 1.4 Modelos del color: RGB, CMY, HSV y HSL

El color se cuantifica mediante modelos matemáticos que definen cómo se mezclan las señales:

* 
**RGB (Red, Green, Blue):** Modelo aditivo utilizado en pantallas digitales. En Blender, este modelo define el color difuso de los materiales mediante componentes RGBA.


* **CMY (Cyan, Magenta, Yellow):** Modelo sustractivo utilizado principalmente en la industria de la impresión.
* **HSV/HSL (Hue, Saturation, Value/Lightness):** Modelos cilíndricos más intuitivos para el diseño humano, separando el tinte del color de su intensidad y brillo.

> ### 💡 Tutorial: Iluminación de un cubo en Blender
> 
> 
> Según los principios de iluminación (Tema 4.2 del programa):
> 1. **Selección del Objeto:** Asegurarse de tener un cubo en la escena (puede generarse proceduralmente ).
> 2. **Adición de Luz:** Se añade una luz tipo `POINT` o `SUN`.
> 3. **Configuración de Intensidad:** Ajustar la energía de la luz (ej. `luz.data.energy = 1000`) para observar la incidencia de los rayos sobre las caras del polígono.
> 
> 

## 1.5 Representación y trazo de líneas y polígonos

Convertir una línea matemática en una cuadrícula de píxeles requiere algoritmos de rasterización:

* **Algoritmo de Bresenham:** Utiliza aritmética de números enteros para determinar qué píxeles deben iluminarse, optimizando el rendimiento.
* 
**Relleno de Polígonos (Tema 4.1):** Proceso de identificar los píxeles internos de una figura cerrada para aplicarles un material o color.



### 1.5.1 Formatos de imagen

* **Mapas de bits (Raster):** Imágenes formadas por píxeles (PNG, JPG). Son ideales para fotografías pero pierden calidad al escalarse.
* **Vectores:** Definiciones matemáticas de puntos y líneas (SVG). Permiten un escalado infinito sin pérdida de resolución.

---

## 🛠️ Portafolio de Ejercicios Prácticos

En este repositorio se incluyen las implementaciones que demuestran la aplicación de la teoría:

### A. Dibujo de un Polígono y la Flor de la Vida

Ejercicios de geometría sagrada y trazo de polígonos donde se aplica la repetición de patrones y el cálculo de vértices en el espacio.

### B. Escenario Procedural Animado

Práctica integral que combina:

* 
**Traslación (Tema 3.3.1):** Posicionamiento automático de bloques en el espacio 3D.


* 
**Escalamiento (Tema 3.3.2):** Modificación de las proporciones de los objetos para crear variedad arquitectónica.


* 
**Gestión de Memoria:** Limpieza automática del entorno antes de cada ejecución para optimizar recursos.



---

## 1.6 Procesamiento de mapas de bits

Consiste en la manipulación directa de la matriz de píxeles:

* **Filtros de Convolución:** Aplicación de matrices (kernels) para detectar bordes o desenfocar imágenes.
* **Transformaciones de Color:** Ajuste de histogramas, brillo y contraste.
**Evidencia**
  <img width="551" height="341" alt="image" src="https://github.com/user-attachments/assets/c63fca05-2777-4112-9470-71d1a4516c6c" />
  Polígono
  <img width="556" height="344" alt="image" src="https://github.com/user-attachments/assets/c6dda86b-44bb-4a57-a084-d157f04f3753" />
  Flor de vida
  
  **Referencias Bibliográficas**

* **Blender Foundation.** (s.f.). *Blender Python API*. [https://docs.blender.org/api/current/](https://docs.blender.org/api/current/) 
* **Hearn, D., Baker, M. P., & Carithers, W.** (2010). *Computer Graphics with OpenGL* (4ta ed.). Pearson. 
* **Hughes, J. F., Van Dam, A., McGuire, M., Sklar, D. F., Foley, J. D., Feiner, S. K., & Akeley, K.** (2014). *Computer Graphics: Principles and Practice* (3ra ed.). Addison-Wesley Professional. 
* **Python Software Foundation.** (2026, 25 de febrero). *Python 3.11.0 documentation*. [https://docs.python.org/3/](https://docs.python.org/3/) 
