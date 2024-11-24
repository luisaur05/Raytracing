from color import Color  # type: ignore
from luz import Light  # type: ignore
from material import MaterialAcuadrado, Material  # type: ignore
from punto import Punto  # type: ignore
from esfera import Esfera  # type: ignore
from vector import Vector  # type: ignore
from cuboo import Cubo  # type: ignore

# Dimensiones de la imagen renderizada
ANCHO = 960
ALTO = 540
IMAGEN_RENDERIZADA = "imagen1CuboEsferas.ppm"

# Posición de la cámara en el espacio 3D
CAMARA = Vector(0, -0.35, -1)

# Lista de objetos en la escena
OBJETOS = [
    # Plano del suelo (Ground Plane)
    Esfera(
        Punto(0, 10000.5, 1),  # Centro del plano (alejado en el eje Y para simular un suelo)
        10000.0,  # Radio extremadamente grande para cubrir la vista
        MaterialAcuadrado(  # Material ajedrezado con colores alternos
            color1=Color.desde_hex("#420500"),  # Color oscuro
            color2=Color.desde_hex("#e6b87d"),  # Color claro
            ambiente=0.2,  # Coeficiente de luz ambiental
            reflexion=0.2,  # Coeficiente de reflexión
        ),
    ),
    # Esfera rosa
    Esfera(
        Punto(1.1, -0.1, 1),  # Centro de la esfera
        0.6,  # Radio
        Material(Color.desde_hex("#803980")),  # Material con color rosa
    ),
    # Esfera azul
    Esfera(
        Punto(-1.55, -0.1, 2.25),  # Centro de la esfera
        0.6,  # Radio
        Material(Color.desde_hex("#0000FF")),  # Material con color azul
    ),
    # Cubo
    Cubo(
        esquina_min=Vector(-0.5, -0.5, 2.5),  # Esquina mínima del cubo
        esquina_max=Vector(0.5, 0.5, 3.5),  # Esquina máxima del cubo
        material=Material(Color.desde_hex("#803980")),  # Material con color rosa
    ),
]

# Lista de luces en la escena
LUCES = [
    # Luz blanca cerca de la cámara
    Light(Punto(1.5, -0.5, -10), Color.desde_hex("#FFFFFF")),
    # Luz difusa con un tono grisáceo
    Light(Punto(-0.5, -10.5, 0), Color.desde_hex("#E6E6E6")),
]
