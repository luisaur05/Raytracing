from color import Color # type: ignore
from imagen import Imagen
from punto import Punto # type: ignore
from rayo import Rayo
import random

class MotorDeRenderizado:
    """Renderiza objetos 3D a objetos 2D usando trazado de rayos"""

    PROFUNDIDAD_MAXIMA = 5
    DESPLAZAMIENTO_MINIMO = 0.0001

    def renderizar(self, escena):
        ancho = escena.ancho
        alto = escena.alto
        razon_aspecto = float(ancho) / alto
        x0 = -1.0
        x1 = +1.0
        paso_x = (x1 - x0) / (ancho - 1)
        y0 = -1.0 / razon_aspecto
        y1 = +1.0 / razon_aspecto
        paso_y = (y1 - y0) / (alto - 1)

        camara = escena.camara
        pixeles = Imagen(ancho, alto)

        for j in range(alto):
            y = y0 + j * paso_y
            for i in range(ancho):
                x = x0 + i * paso_x
                rayo = Rayo(camara, Punto(x, y) - camara)
                pixeles.establecer_pixel(i, j, self.trazar_rayo(rayo, escena))
            print("{:3.0f}%".format(float(j) / float(alto) * 100), end="\r")
        return pixeles

    def trazar_rayo(self, rayo, escena, profundidad=0):
        color = Color(0, 0, 0)
        # Encuentra el objeto más cercano impactado por el rayo en la escena
        distancia_hit, objeto_hit = self.encontrar_objeto_mas_cercano(rayo, escena)
        if objeto_hit is None:
            # Fondo de atardecer con degradado
            return self.color_cielo(rayo.direccion)
        pos_hit = rayo.origen + rayo.direccion * distancia_hit
        normal_hit = objeto_hit.normal(pos_hit)
        color += self.color_en_posicion(objeto_hit, pos_hit, normal_hit, escena)
        if profundidad < self.PROFUNDIDAD_MAXIMA:
            nueva_pos_rayo = pos_hit + normal_hit * self.DESPLAZAMIENTO_MINIMO
            nueva_dir_rayo = (
                rayo.direccion - 2 * rayo.direccion.producto_punto(normal_hit) * normal_hit
            )
            nuevo_rayo = Rayo(nueva_pos_rayo, nueva_dir_rayo)
            # Atenuar el rayo reflejado por el coeficiente de reflexión
            color += (
                self.trazar_rayo(nuevo_rayo, escena, profundidad + 1) * objeto_hit.material.reflexion
            )
        return color

    def color_cielo(self, direccion):
        """
        Devuelve el color del cielo según la dirección del rayo.
        - direccion.y: determina la altura del rayo (de -1 a 1)
        """
        t = (direccion.y + 1) / 2  # Normaliza y (altura) a [0, 1]

        # Colores del degradado (11 colores)
        colores = [
            Color.desde_hex("#87CEEB"),  # Azul cielo
            Color.desde_hex("#4682B4"),  # Azul acero
            Color.desde_hex("#1E90FF"),  # Azul profundo
            Color.desde_hex("#1E90FF"),  # Azul profundo
            Color.desde_hex("#6A5ACD"),  # Azul violeta
            Color.desde_hex("#000000"),  # Negro
            Color.desde_hex("#FF4500"),  # Naranja
            Color.desde_hex("#FF6347"),  # Rojo tomate
            Color.desde_hex("#FFA07A"),  # Salmón claro
            Color.desde_hex("#FFD700"),  # Dorado
            Color.desde_hex("#EEE8AA"),  # Amarillo claro
        ]

        # Dividir el cielo en 10 bandas (11 colores => 10 transiciones)
        num_bandas = len(colores) - 1
        indice_banda = int(t * num_bandas)  # Índice de la banda actual
        t_banda = (t * num_bandas) - indice_banda  # Progreso dentro de la banda actual

        # Asegurar que no exceda el índice válido
        if indice_banda >= num_bandas:
            indice_banda = num_bandas - 1
            t_banda = 1
        # Interpolar entre los dos colores de la banda actual
        color_base = colores[indice_banda] * (1 - t_banda) + colores[indice_banda + 1] * t_banda

        # Agregar estrellas
        if random.random() < 0.002:  # Probabilidad del 0.2% de una estrella
            brillo_estrella = random.uniform(0.7, 1.0)  # Brillo aleatorio para la estrella
            color_estrella = Color(brillo_estrella, brillo_estrella, brillo_estrella)
            color_base += color_estrella

        return color_base
    
    def encontrar_objeto_mas_cercano(self, rayo, escena):
        distancia_min = None
        objeto_hit = None
        for objeto in escena.objetos:
            distancia = objeto.intersecta(rayo)
            if distancia is not None and (objeto_hit is None or distancia < distancia_min):
                distancia_min = distancia
                objeto_hit = objeto
        return (distancia_min, objeto_hit)

    def color_en_posicion(self, objeto_hit, pos_hit, normal, escena):
        material = objeto_hit.material
        color_objeto = material.color_en(pos_hit)
        a_camara = escena.camara - pos_hit
        especular_k = 50
        color = material.ambiente * Color.desde_hex("#000000")
        # Cálculos de iluminación
        for luz in escena.luces:
            a_luz = Rayo(pos_hit, luz.posicion - pos_hit)
            # Sombreado difuso (Lambert)
            color += (
                color_objeto
                * material.difuso
                * max(normal.producto_punto(a_luz.direccion), 0)
            )
            # Sombreado especular (Blinn-Phong)
            vector_medio = (a_luz.direccion + a_camara).normalizar()
            color += (
                luz.color
                * material.especular
                * max(normal.producto_punto(vector_medio), 0) ** especular_k
            )
        return color