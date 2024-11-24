from vector import Vector  


class Color(Vector):
    """
    Almacena colores como tripletas RGB. Es un alias para Vector.
    """

    @classmethod
    def desde_hex(cls, color_hex="#000000"):
        """
        Crea un objeto Color a partir de un valor hexadecimal.

        Args:
            color_hex (str): Cadena que representa un color en formato hexadecimal.
                             Ejemplo: "#FF00FF".

        Returns:
            Color: Objeto Color con componentes RGB normalizadas entre 0 y 1.
        """
        # Convierte los componentes hexadecimales en valores flotantes entre 0 y 1
        rojo = int(color_hex[1:3], 16) / 255.0
        verde = int(color_hex[3:5], 16) / 255.0
        azul = int(color_hex[5:7], 16) / 255.0
        return cls(rojo, verde, azul)
