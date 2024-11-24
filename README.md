# Proyecto de Ray Tracing en Python

Este es un proyecto de ray tracing en Python que implementa un motor básico para renderizar escenas 3D, simulando cómo la luz interactúa con los objetos en una escena tridimensional. El motor calcula la trayectoria de los rayos de luz que impactan sobre los objetos, determinando su color y sombras, y generando una imagen de salida.


## Descripción

El motor de **Ray Tracing** simula la propagación de la luz en una escena tridimensional, calculando la interacción de los rayos de luz con los objetos, lo que permite generar imágenes realistas. El proceso básico implica trazar rayos desde la cámara hacia los objetos en la escena, calcular las intersecciones con estos objetos y determinar el color final de cada píxel basado en varias interacciones de luz.

El cálculo de los colores y sombras se realiza mediante varios modelos de iluminación y reflexión. A continuación, se describen las interacciones de luz clave:

### Cálculo de Color y Reflexión

1. **Cálculo de Intersección de Rayos**: 
   Cada rayo proyectado desde la cámara se interseca con los objetos en la escena. Cuando un rayo impacta con un objeto, el motor calcula el punto de intersección y determina las propiedades de ese objeto en ese punto, como su color base, normal a la superficie y material.

2. **Modelo de Iluminación**:
   Una vez que se ha encontrado la intersección de un rayo con un objeto, se calcula cómo la luz de las fuentes en la escena incide en ese punto de la superficie. El motor utiliza el modelo de **iluminación de Phong** para modelar cómo la luz se refleja en la superficie. Este modelo considera tres componentes principales:
   
   - **Difusa**: La luz que incide de manera uniforme sobre la superficie, en función del ángulo entre la dirección de la luz y la normal a la superficie. Esta componente se calcula con el **producto punto** entre la normal de la superficie y la dirección de la luz, ajustado por la intensidad de la fuente de luz.
   
   - **Especular**: La luz que refleja la luz de manera especular (similar a un reflejo en una superficie pulida), que depende del ángulo entre la dirección de la luz, la normal de la superficie y la dirección de la cámara. Esta componente se calcula utilizando el **producto punto** entre el vector reflejado y el vector de visión, elevando el valor a una potencia especular para simular la concentración de la reflexión.

   - **Ambiental**: Esta componente modela la luz ambiental que ilumina toda la escena de manera uniforme, independientemente de la posición relativa entre la fuente de luz y los objetos.

   La fórmula general para el cálculo de color con el modelo de Phong es:

   ```python
   color = color_ambiental + color_difuso + color_especular
   ```

   donde:
   - `color_ambiental` es la luz que afecta a todos los objetos por igual.
   - `color_difuso` se calcula como el producto entre la intensidad de la luz y el coseno del ángulo entre la normal y la dirección de la luz.
   - `color_especular` se calcula en función del ángulo entre el vector de reflexión y la dirección del ojo/cámara.



### Archivos principales:

- **`color.py`**: Define la clase `Color`, que se encarga de representar y manipular colores en formato RGB.
- **`cuboo.py`**: Representa un objeto de tipo cubo, utilizado como ejemplo de objeto 3D.
- **`engine.py`**: Contiene la clase `MotorDeRenderizado`, que es el motor principal para el renderizado de la escena. Se encarga de trazar los rayos, encontrar las intersecciones con los objetos y calcular el color final.
- **`image.py`**: Define la clase `Imagen`, que se utiliza para almacenar los píxeles de la imagen generada y guardar la imagen en formato PPM.
- **`light.py`**: Representa una fuente de luz en la escena, con propiedades de posición y color.
- **`main.py`**: El archivo principal que ejecuta el programa. Carga una escena desde un archivo, crea el motor de ray tracing, genera la imagen y la guarda en un archivo de salida.
- **`ray.py`**: Define la clase `Rayo`, que representa un rayo de luz con una posición de origen y una dirección.
- **`scene.py`**: Representa la escena 3D, que contiene la cámara, los objetos, las luces y las dimensiones de la imagen.
- **`material.py`**: Define los materiales con los que los objetos interactúan, como colores base, reflectividad, difusividad, etc.
- **`point.py`**: Define la clase `Punto`, que es una subclase de `Vector` para representar posiciones en el espacio 3D.
- **`sphere.py`**: Representa un objeto de tipo esfera, un ejemplo básico de forma 3D.
- **`vector.py`**: Define la clase `Vector`, utilizada para representar y operar con vectores 3D en cálculos de geometría y física.

## Requisitos

- Python 3.x
- No se requiere ninguna librería externa solo las ya mencionadas que creamos; el código está escrito utilizando solo bibliotecas estándar de Python.

## Ejecución del Proyecto

Para ejecutar el proyecto, usa el siguiente comando desde la terminal:

```bash
python3 main.py examples.ejemplo1
```

Este comando ejecutará el script `main.py`, que cargará el archivo de escena `examples.ejemplo1`, procesará la escena con el motor de ray tracing y generará una imagen en el formato PPM.

### Explicación del comando:
- **`python3`**: Es la ruta al intérprete de Python 3.
- **`main.py`**: Es la ruta al archivo principal que ejecuta el ray tracing (dependiendo tu equipo).
- **`examples.ejemplo1`**: Es un archivo de escena que define la cámara, los objetos (en este caso, esferas) y las luces de la escena. Este archivo debe estar disponible en el directorio correspondiente.



## Archivos de Escena

El archivo de escena (por ejemplo, `examples.ejemplo1`) define todos los elementos de la escena, como la cámara, los objetos (esferas, cubos, planos, etc.), las luces y las dimensiones de la imagen. Un ejemplo básico de escena podría ser:

```python
# Definición de la escena

CAMARA = Punto(0, 0, -5)
ANCHO = 800
ALTO = 600
IMAG_RENDERIZADA = "output.ppm"

LUCES = [
    Light(Punto(0, 5, -5), Color.desde_hex("#FFFFFF")),
]

OBJETOS = [
    Sphere(Point(0, 0, 0), 1.0,Punto(0, 0, 0), 1.0, Material(color=Color.desde_hex("#FF0000"))),
    Sphere(Point(2, 0, 0), 1.0,Punto(2, 0, 0), 1.0, Material(color=Color.desde_hex("#00FF00"))),
]
```

En este ejemplo, se define una cámara, dos esferas y una luz. La escena será renderizada y la imagen final se guardará en `output.ppm`.

## Observaciones

Contamos con dos ejemplos de imagenes:

-  **`ejemplo1.py`**: Este archivo es un ejemplo de RayTracer con tres esferas y un cubo, donde añadimos dos luces y un fondo degradado con estrellas.
- **`ejemplo2.py`**:  Este ejemplo utiliza una estructura de esferas para formar un modelo de un oso. En este archivo, usarás varias esferas para crear las diferentes partes del oso (cabeza, cuerpo, patas, etc.) .

