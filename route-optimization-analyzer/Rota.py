#Felipe Lemos Ferreira 174483
#Gabriel Zanchetim da Silva 173058
#Rian Julian Braga Kokeny 260664
#A melhoria da funcao "otimiza" foi feita aqui, dentro da classe "Rota", não no código "TarefaAula8.py"

import random
import time
from Coordenada import Coordenada
from PIL import Image, ImageDraw

class Rota:
    def __init__(self):
        self.coords = []

    def addCoord(self, coord):
        self.coords.append(coord)

    def comprimento(self):
        length = 0
        for i in range(len(self.coords)):
            length += self.coords[i].distancia(self.coords[(i + 1) % len(self.coords)])
        return length

    def copy(self):
        new_rota = Rota()
        for coord in self.coords:
            new_rota.addCoord(Coordenada((coord.x, coord.y)))
        return new_rota

    def shuffle(self):
        random.shuffle(self.coords)

    def __str__(self):
        return "->".join(str(coord) for coord in self.coords) + "->" + str(self.coords[0])

    def espera(self, t):
        tin = time.time()
        delta = 0
        aux = -1
        while delta < t:
            delta = (time.time() - tin) * 1000
            if delta >= (aux + 1) and delta < t:
                aux += 1000
                print(f"Esperando: {int((aux + 1)):.0f}ms")

    def otimiza(self):
        for i in range(len(self.coords)):
            for j in range(i + 1, len(self.coords)):
                rota_temp = self.copy()
                rota_temp.coords[i], rota_temp.coords[j] = rota_temp.coords[j], rota_temp.coords[i]
                if rota_temp.comprimento() < self.comprimento():
                    self.coords = rota_temp.coords

    def randomCoords(self, n, max_coord):
        self.coords = [Coordenada((random.randint(1, max_coord), random.randint(1, max_coord))) for _ in range(n)]

    def maximo(self):
        max_x = max(coord.x for coord in self.coords)
        max_y = max(coord.y for coord in self.coords)
        return (max_x, max_y)

    def desenha(self, filename):
        max_x, max_y = self.maximo()
        image = Image.new("RGB", (max_x + 50, max_y + 50), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        for i in range(len(self.coords)):
            coord1 = self.coords[i]
            coord2 = self.coords[(i + 1) % len(self.coords)]
            draw.line([(coord1.x, coord1.y), (coord2.x, coord2.y)], fill=(0, 0, 0), width=2)

        draw.text((max_x // 2, max_y + 10), f"Comprimento: {self.comprimento()}", fill=(0, 0, 0))
        image.save(filename)
        return image