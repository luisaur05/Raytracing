from vector import Vector  

class Cubo:
    def __init__(self, esquina_min, esquina_max, material):
        # Verifica que las esquinas sean instancias de la clase Vector
        if not isinstance(esquina_min, Vector) or not isinstance(esquina_max, Vector):
            raise ValueError("esquina_min y esquina_max deben ser instancias de Vector")

        # Verifica que los límites mínimos sean menores que los máximos en cada eje
        if (esquina_min.x >= esquina_max.x or 
            esquina_min.y >= esquina_max.y or 
            esquina_min.z >= esquina_max.z):
            raise ValueError("esquina_min debe ser menor que esquina_max en todos los ejes")
        
        # Asigna los valores iniciales a las propiedades del cubo
        self.esquina_min = esquina_min  # Límite inferior (Vector(xMin, yMin, zMin))
        self.esquina_max = esquina_max  # Límite superior (Vector(xMax, yMax, zMax))
        self.material = material  # Material asociado al cubo

    def intersecta(self, rayo):
        # Calcula las intersecciones en el eje X
        tx1 = (self.esquina_min.x - rayo.origen.x) / rayo.direccion.x
        tx2 = (self.esquina_max.x - rayo.origen.x) / rayo.direccion.x

        # Calcula las intersecciones en el eje Y
        ty1 = (self.esquina_min.y - rayo.origen.y) / rayo.direccion.y
        ty2 = (self.esquina_max.y - rayo.origen.y) / rayo.direccion.y

        # Calcula las intersecciones en el eje Z
        tz1 = (self.esquina_min.z - rayo.origen.z) / rayo.direccion.z
        tz2 = (self.esquina_max.z - rayo.origen.z) / rayo.direccion.z

        # Encuentra los límites cercanos (mínimos) y lejanos (máximos) en cada eje
        t_cerca = max(min(tx1, tx2), min(ty1, ty2), min(tz1, tz2))  # Máximo de los mínimos
        t_lejos = min(max(tx1, tx2), max(ty1, ty2), max(tz1, tz2))  # Mínimo de los máximos

        # Verifica si no hay intersección:
        # 1. Si el límite cercano es mayor que el lejano, el rayo no atraviesa el cubo.
        # 2. Si el límite lejano es menor que 0, el cubo está detrás del origen del rayo.
        if t_cerca > t_lejos or t_lejos < 0:
            return None  # No hay intersección

        # Devuelve la distancia de la intersección más cercana en el frente del rayo
        return t_cerca if t_cerca > 0 else t_lejos

    def normal(self, punto_superficie):
        # Calcula el centro del cubo sumando las esquinas mínima y máxima, y dividiendo entre 2
        centro = (self.esquina_min + self.esquina_max) * 0.5

        # Calcula el vector local desde el punto de superficie hasta el centro
        punto_local = punto_superficie - centro

        # Encuentra el eje con la mayor distancia absoluta
        # Esto indica qué cara del cubo se está intersectando
        eje_max = max(abs(punto_local.x), abs(punto_local.y), abs(punto_local.z))

        # Determina la normal según el eje con mayor contribución
        if abs(punto_local.x) == eje_max:
            # La normal apunta en la dirección del eje X
            return Vector(1 if punto_local.x > 0 else -1, 0, 0)
        elif abs(punto_local.y) == eje_max:
            # La normal apunta en la dirección del eje Y
            return Vector(0, 1 if punto_local.y > 0 else -1, 0)
        else:
            # La normal apunta en la dirección del eje Z
            return Vector(0, 0, 1 if punto_local.z > 0 else -1)