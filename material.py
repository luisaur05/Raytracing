from color import Color  # type: ignore


class Material:
    """El material tiene un color y propiedades que determinan cómo reacciona a la luz"""

    def __init__(
        self,
        color=Color.desde_hex("#FFFFFF"),
        ambiente=0.05,  # Renombrado 'ambient' a 'ambiente'
        difuso=1.0,  # Renombrado 'diffuse' a 'difuso'
        especular=1.0,  # Renombrado 'specular' a 'especular'
        reflexion=0.5,  # Renombrado 'reflection' a 'reflexion'
    ):
        self.color = color
        self.ambiente = ambiente
        self.difuso = difuso
        self.especular = especular
        self.reflexion = reflexion

    def color_en(self, posicion):
        """Devuelve el color del material en una posición dada"""
        return self.color


class MaterialAcuadrado:
    """Material con un patrón de tablero de ajedrez basado en dos colores"""

    def __init__(
        self,
        color1=Color.desde_hex("#FFFFFF"),
        color2=Color.desde_hex("#000000"),
        ambiente=0.05,  # Renombrado 'ambient' a 'ambiente'
        difuso=1.0,  # Renombrado 'diffuse' a 'difuso'
        especular=1.0,  # Renombrado 'specular' a 'especular'
        reflexion=0.5,  # Renombrado 'reflection' a 'reflexion'
    ):
        self.color1 = color1
        self.color2 = color2
        self.ambiente = ambiente
        self.difuso = difuso
        self.especular = especular
        self.reflexion = reflexion

    def color_en(self, posicion):
        """Devuelve el color en una posición, alternando entre dos colores como un patrón de ajedrez"""
        if int((posicion.x + 5.0) * 3.0) % 2 == int(posicion.z * 3.0) % 2:
            return self.color1
        else:
            return self.color2
