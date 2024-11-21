#Felipe Lemos Ferreira      174483
#Gabriel Zanchetim da Silva 173058
#Rian Júlian Braga Kokeny   260664

import operator
import random

carro = dict()
filename = "carros.txt"

def addCarro(carro):
    with open(filename, "a") as file:
        carro_str=f"placa: {(carro['placa'])}, ano: {carro['ano']}, marca: {carro['marca']}, modelo: {carro['modelo']}\n"
        file.write(carro_str)
    print("add:", str(carro))

def carregaCarros():
    carros = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            carro = {}
            for part in parts:
                key, value = part.split(": ")
                carro[key] = value
            carros.append(carro)
    return carros

def verificaPlaca(placa):
    carros = carregaCarros()
    for carro in carros:
        if carro["placa"] == placa:
            print("contém placa" + placa)
            return True
        return False

def placaAleatoria():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; numeros = "0123456789"; existe = True

    while existe:
        placa = ""
        for _ in range(3):
            placa += random.choice(letras)
        placa += random.choice(numeros)
        placa += random.choice(letras)
        for _ in range(2):
            placa += random.choice(numeros)

        if verificaPlaca(placa):
            print("Placa já existe")
        else:
            existe = False
            return placa

def carroAleatorio():
    marcas = ["chevrolet", "volkswagen", "fiat"]
    modelos = {
        "chevrolet": ["onix", "cruze", "camaro"],
        "volkswagen": ["polo", "jetta", "gol"],
        "fiat": ["pulse", "argo", "moby"]
    }

    placa = placaAleatoria()
    marca = random.choice(marcas)
    modelo = random.choice(modelos[marca])
    ano = random.randint(1999, 2023)

    carro = {
        "placa": placa,
        "ano": ano,
        "marca": marca,
        "modelo": modelo
    }
    return carro

def populaDados():
    with open(filename, "w") as file:
        for _ in range(200):
            carro = carroAleatorio()
            addCarro(carro)

def manualAddCarro():
    placa = input("Digite a placa: ")
    ano = int(input("Digite ano: "))
    marca = input("Digite marca: ")
    modelo = input("Digite Modelo: ")
    addCarro({"placa": placa, "ano": ano, "marca": marca, "modelo": modelo})

def calculaEstatistica(chave):
    carros = carregaCarros()
    print(f"\n -- Numeros de carros por {chave}")

    soma = {}
    for carro in carros:
        valorChave = carro[f"{chave}"]
        if valorChave in soma:
            soma[valorChave] += 1
        else:
            soma[valorChave] = 1
    for chaveSoma, valorSoma in sorted(soma.items(), key=operator.itemgetter(1)):
        print("{} {} : {} {}(s)".format(chave, chaveSoma, valorSoma, chave))

def geraEstatistica():
    calculaEstatistica("ano")
    calculaEstatistica("marca")
    calculaEstatistica("modelo")

populaDados()
manualAddCarro()
geraEstatistica()