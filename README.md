# Ray Tracing Project in Python

This project is a Ray Tracing implementation in Python that simulates a basic engine to render 3D scenes, modeling how light interacts with objects in a three-dimensional space. The engine calculates the path of light rays hitting objects, determining their color and shadows, and generating an output image.

## Description

The **Ray Tracing** engine simulates light propagation in a 3D scene by calculating the interaction of light rays with objects, enabling the creation of realistic images. The process involves tracing rays from the camera to objects in the scene, calculating intersections with these objects, and determining the final color of each pixel based on various light interactions.

The color and shadow calculations are performed using multiple lighting and reflection models. Below are the key light interactions:

### Color and Reflection Calculation

1. **Ray-Object Intersection Calculation**:  
   Each `rayo` projected from the camera intersects with objects in the scene. When a `rayo` hits an object, the engine computes the intersection point and determines the properties of the object at that point, such as its base color, surface normal, and material.

2. **Lighting Model**:  
   Once a `rayo`-object intersection is found, the engine calculates how the scene's light sources affect that surface point. The engine uses the **Phong lighting model** to simulate light reflection on the surface. This model considers three main components:

   - **Difuso**: Light uniformly incident on the surface, depending on the angle between the light direction and the surface normal. This component is calculated using the **dot product** between the surface normal and the light direction, adjusted by the light source's intensity.

   - **Especular**: Light reflecting specularly (like a mirror reflection), which depends on the angle between the light direction, the surface normal, and the camera direction. This component is calculated using the **dot product** between the reflected vector and the view vector, raised to a specular power to simulate concentrated reflection.

   - **Ambiental**: This component models ambient light that illuminates the entire scene uniformly, regardless of the relative positions of light sources and objects.

   The general formula for color calculation using the Phong model is:

   ```python
   color = color_ambiental + color_difuso + color_especular
Where:
- `color_ambiental` is the light affecting all objects equally.
- `color_difuso` is calculated as the product of light intensity and the cosine of the angle between the normal and the light direction.
- `color_especular` depends on the angle between the reflection vector and the camera direction.

### Main Files:

- **`color.py`**: Defines the `Color` class to represent and manipulate RGB colors.
- **`cuboo.py`**: Represents a cube object used as an example of a 3D object.
- **`engine.py`**: Contains the `MotorDeRenderizado` class, which is the main engine for scene rendering. It traces rays, finds intersections with objects, and computes the final color.
- **`image.py`**: Defines the `Imagen` class to store pixels of the generated image and save the image in PPM format.
- **`light.py`**: Represents a light source in the scene, with position and color properties.
- **`main.py`**: The main file that runs the program. It loads a scene from a file, creates the ray tracing engine, generates the image, and saves it to an output file.
- **`ray.py`**: Defines the `Rayo` class to represent a ray of light with an origin position and direction.
- **`scene.py`**: Represents the 3D scene containing the camera, objects, lights, and image dimensions.
- **`material.py`**: Defines the materials that objects interact with, such as base colors, reflectivity, diffusivity, etc.
- **`point.py`**: Defines the `Punto` class, a subclass of `Vector` for representing positions in 3D space.
- **`sphere.py`**: Represents a sphere object, a basic example of a 3D shape.
- **`vector.py`**: Defines the `Vector` class used to represent and operate with 3D vectors in geometry and physics calculations.

## Requirements

- Python 3.x  
- No external libraries are required; the code uses only Python's standard libraries.

## Running the Project

To execute the project, use the following command in the terminal:

```bash
python3 main.py examples.ejemplo1
```

This command runs the `main.py` script, which loads the `examples.ejemplo1` scene file, processes the scene with the ray tracing engine, and generates an image in PPM format.

### Command Explanation:
- **`python3`**: Path to the Python 3 interpreter.
- **`main.py`**: Path to the main file running the ray tracing engine (depending on your system).
- **`examples.ejemplo1`**: A scene file defining the camera, objects (e.g., spheres), and lights in the scene. This file must be available in the appropriate directory.

## Scene Files

A scene file (e.g., `examples.ejemplo1`) defines all elements of the scene, such as the camera, objects (spheres, cubes, planes, etc.), lights, and image dimensions. A basic scene example might look like this:

```python
# Scene definition

CAMARA = Punto(0, 0, -5)
ANCHO = 800
ALTO = 600
IMAG_RENDERIZADA = "output.ppm"

LUCES = [
    Light(Punto(0, 5, -5), Color.from_hex("#FFFFFF")),
]

OBJETOS = [
    Sphere(Punto(0, 0, 0), 1.0, Material(color=Color.from_hex("#FF0000"))),
    Sphere(Punto(2, 0, 0), 1.0, Material(color=Color.from_hex("#00FF00"))),
]
```

In this example, a camera, two spheres, and a light source are defined. The scene is rendered, and the final image is saved to `output.ppm`.

## Notes

We provide two example scenes:

- **`ejemplo1.py`**: This file is an example RayTracer with three spheres and a cube, where we add two lights and a gradient background with stars.
- **`ejemplo2.py`**: This example uses a structure of spheres to create a bear model. It employs several spheres to represent the bear's different parts (head, body, legs, etc.).
