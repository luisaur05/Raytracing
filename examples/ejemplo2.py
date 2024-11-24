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
IMAGEN_RENDERIZADA = "imagenOsoDePie.ppm"

# Posición de la cámara en el espacio 3D
CAMARA = Vector(0, -0.35, -3)

# Lista de objetos en la escena
OBJETOS = [
    # Plano del suelo
    Esfera(
        Punto(0, 10000.5, 1),
        10000.0,
        MaterialAcuadrado(
            color1=Color.desde_hex("#420500"),
            color2=Color.desde_hex("#e6b87d"),
            ambiente=0.2,
            reflexion=0.2,
        ),
    ),
    
    # Cuerpo del oso (esfera grande para el torso)
    Esfera(
        Punto(0, 0, 1),
        0.15,
        Material(Color.desde_hex("#8B4513")),
    ),
    
    # Cabeza del oso (esfera sobre el cuerpo)
    Esfera(
        Punto(0, 0.225, 1),
        0.1,
        Material(Color.desde_hex("#8B4513")),
    ),
    
    # Pata izquierda
    Esfera(
        Punto(-0.0875, 0.35, 1),
        0.05,
        Material(Color.desde_hex("#8B4513")),
    ),
    
    # Pata derecha
    Esfera(
        Punto(0.0875, 0.35, 1),
        0.05,
        Material(Color.desde_hex("#8B4513")),
    ),
    
    # Mano derecha
    Esfera(
        Punto(0.12, 0.2, 1),
        0.05,
        Material(Color.desde_hex("#8B4513")),
    ),
    
    # Mano izquierda
    Esfera(
        Punto(-0.12, 0.2, 1),
        0.05,
        Material(Color.desde_hex("#8B4513")),
    ),
    
    # Oreja izquierda
    Esfera(
        Punto(-0.075, -0.15, 1),
        0.0375,
        Material(Color.desde_hex("#8B4513")),
    ),
    
    # Oreja derecha
    Esfera(
        Punto(0.075, -0.15, 1),
        0.0375,
        Material(Color.desde_hex("#8B4513")),
    ),
]

# Lista de luces en la escena
LUCES = [
    Light(Punto(1.5, -0.5, -10), Color.desde_hex("#FFFFFF")),
    Light(Punto(-0.5, -10.5, 0), Color.desde_hex("#E6E6E6")),
]