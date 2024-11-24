from color import Color  # type: ignore

class Light:
    """Luz representa una fuente de luz puntual de un color determinado."""

    def __init__(self, posicion, color=Color.desde_hex("#FFFFFF")):
        self.posicion = posicion
        self.color = color
