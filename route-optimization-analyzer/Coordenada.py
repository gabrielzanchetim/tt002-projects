class Coordenada:
    def __init__(self, ponto=(0, 0)):
        if not isinstance(ponto, tuple) or len(ponto) != 2:
            raise Exception("Número de argumentos errado: 2")
        if not all(isinstance(x, (int, float)) for x in ponto):
            raise Exception("Elemento da tupla não é int or float")
        self.x, self.y = ponto

    def distancia(self, outra_coord):
        return ((self.x - outra_coord.x) ** 2 + (self.y - outra_coord.y) ** 2) ** 0.5

    def __str__(self):
        return f"({self.x}, {self.y})"