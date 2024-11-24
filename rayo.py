class Rayo:
    """El Rayo es una semirrecta con un origen y una direccioon normalizada"""

    def __init__(self, origen, direccion):
        self.origen = origen
        self.direccion = direccion.normalizar()
