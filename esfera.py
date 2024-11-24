from math import sqrt 

class Esfera:
    def __init__(self, centro, radio, material):
        self.centro = centro  
        self.radio = radio  
        self.material = material 

    def intersecta(self, rayo):
        # Vector que va desde el centro de la esfera hasta el origen del rayo
        esfera_a_rayo = rayo.origen - self.centro

        # Coeficiente b del polinomio cuadrático. Se calcula como el doble del producto
        # escalar entre la dirección del rayo y el vector esfera_a_rayo.
        b = 2 * rayo.direccion.producto_punto(esfera_a_rayo)

        # Coeficiente c del polinomio cuadrático. Es la magnitud al cuadrado del vector
        # esfera_a_rayo, menos el cuadrado del radio de la esfera.
        c = esfera_a_rayo.producto_punto(esfera_a_rayo) - self.radio * self.radio

        # Discriminante de la ecuación cuadrática. Determina si hay intersecciones:
        # - Si discriminante < 0: No hay soluciones reales (no hay intersección).
        # - Si discriminante >= 0: Hay una o dos soluciones reales.
        discriminante = b * b - 4 * c

        if discriminante >= 0:
            # Calcula la distancia a la intersección más cercana usando la fórmula cuadrática
            distancia = (-b - sqrt(discriminante)) / 2

            # Si la distancia es positiva, el punto de intersección está en frente del rayo
            if distancia > 0:
                return distancia

        # Si el discriminante es negativo o la intersección está detrás del origen del rayo,
        # no hay intersección válida.
        return None

    def normal(self, punto_superficie):
        # La normal se obtiene restando el centro de la esfera al punto de la superficie
        # y normalizando el resultado.
        return (punto_superficie - self.centro).normalizar()