#Gabriel Zanchetim da Silva 173058
#Felipe Lemos Ferreira 174483
#Rian Julia Braga Kokeny 260664

from PIL import Image, ImageDraw

coordenadas = []
with open("coordenadas.txt", "r") as file:
    for line in file:
        nome, estado, sigla, latitude, longitude = line.strip().split(";")
        coordenadas.append({
            "nome": nome,
            "estado": estado,
            "sigla": sigla,
            "latitude": float(latitude),
            "longitude": float(longitude)
        })

cores_estados = {
    "Rio Grande do Sul": "lightgrey",
    "Parana": "lightgrey",
    "Rio de Janeiro": "lightgrey",
    "Goias": "lightgrey",
    "Sergipe": "lightgrey",
    "Pernambuco": "lightgrey",
    "Rio Grande do Norte": "lightgrey",
    "Maranhao": "lightgrey",
    "Santa Catarina": "yellow",
    "Sao Paulo": "yellow",
    "Espirito Santo": "yellow",
    "Paraiba": "yellow",
    "Tocantins": "yellow",
    "Amazonas": "yellow",
    "Mato Grosso do Sul": "blue",
    "Bahia": "blue",
    "Alagoas": "yellow",
    "Ceara": "blue",
    "Para": "blue",
    "Rondonia": "blue",
    "Minas Gerais": "black",
    "Piaui": "black",
    "Mato Grosso": "black",
    "Acre": "black",
    "Roraima": "black",
    "Amapa": "black",
    "Distrito Federal" : "blue",
    "NA" : "lightgrey"
}

min_latitude = min(coordenadas, key=lambda x: x["latitude"])["latitude"]
max_latitude = max(coordenadas, key=lambda x: x["latitude"])["latitude"]
min_longitude = min(coordenadas, key=lambda x: x["longitude"])["longitude"]
max_longitude = max(coordenadas, key=lambda x: x["longitude"])["longitude"]

img = Image.new("RGB", (1001, 1001), "white")
draw = ImageDraw.Draw(img)

def normalize_coordinate(coordinate, min_value, max_value):
    return int(1000 * (coordinate - min_value) / (max_value - min_value))

for coord in coordenadas:
    estado = coord["estado"]
    cor = cores_estados[estado]
    x = normalize_coordinate(coord["longitude"], min_longitude, max_longitude)
    y = 1000 - normalize_coordinate(coord["latitude"], min_latitude, max_latitude)
    draw.point((x, y), fill=cor)

img.save("Brasil.png")
