class Imagen:
    def __init__(self, ancho, alto):
        """Inicializa la imagen con el ancho y alto proporcionados."""
        self.ancho = ancho
        self.alto = alto
        # Crea una matriz de píxeles vacíos (None) con las dimensiones dadas.
        self.pixels = [[None for _ in range(ancho)] for _ in range(alto)]

    def establecer_pixel(self, x, y, color):
        """Establece el color del píxel en las coordenadas (x, y)."""
        self.pixels[y][x] = color

    def escribir_ppm(self, archivo_imagen):
        """Escribe la imagen en formato PPM en el archivo dado."""
        # Convierte un valor de color a byte (entre 0 y 255).
        def a_byte(c):
            return round(max(min(c * 255, 255), 0))

        # Escribe el encabezado del archivo PPM (ancho, alto y valor máximo de color).
        archivo_imagen.write("P3 {} {}\n255\n".format(self.ancho, self.alto))
        for fila in self.pixels:
            for color in fila:
                # Escribe los valores RGB de cada píxel en el archivo.
                archivo_imagen.write(
                    "{} {} {} ".format(
                        a_byte(color.x), a_byte(color.y), a_byte(color.z)
                    )
                )
            archivo_imagen.write("\n")
