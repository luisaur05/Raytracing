import argparse
import importlib
import os
from motor import MotorDeRenderizado  # Ajustado para reflejar el nombre en español
from escena import Escena  # Ajustado para reflejar el nombre en español


def principal():
    parser = argparse.ArgumentParser()
    parser.add_argument("escena", help="Ruta al archivo de escena (sin la extensión .py)")
    args = parser.parse_args()
    
    # Cargar el módulo de la escena
    mod = importlib.import_module(args.escena)

    # Crear la escena usando los parámetros del módulo cargado
    escena = Escena(mod.CAMARA, mod.OBJETOS, mod.LUCES, mod.ANCHO, mod.ALTO)
    
    # Inicializar el motor de renderizado y renderizar la imagen
    motor = MotorDeRenderizado()
    imagen = motor.renderizar(escena)

    # Guardar la imagen en el archivo especificado en el módulo
        
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    with open(mod.IMAGEN_RENDERIZADA, "w") as img_file:
        imagen.escribir_ppm(img_file)


if __name__ == "__main__":
    principal()
