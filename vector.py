import math


class Vector:
    """Un vector de tres elementos usado en gráficos 3D para múltiples propósitos"""

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def producto_punto(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z

    def magnitud(self):
        return math.sqrt(self.producto_punto(self))

    def normalizar(self):
        return self / self.magnitud()

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def __mul__(self, otro):
        assert not isinstance(otro, Vector)
        return Vector(self.x * otro, self.y * otro, self.z * otro)

    def __rmul__(self, otro):
        return self.__mul__(otro)

    def __truediv__(self, otro):
        assert not isinstance(otro, Vector)
        return Vector(self.x / otro, self.y / otro, self.z / otro)