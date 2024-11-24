class Escena:
    """La escena contiene toda la información necesaria para el motor de ray tracing"""

    def __init__(self, camara, objetos, luces, ancho, alto):
        self.camara = camara
        self.objetos = objetos
        self.luces = luces
        self.ancho = ancho
        self.alto = alto
