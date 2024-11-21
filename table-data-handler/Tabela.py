from Linha import Linha
class Tabela:
    def __init__(self, arquivo=None):
        self.cabecalho = Linha()
        self.dados = []

        if arquivo:
            self.carregar_de_arquivo(arquivo)

    def add_cabecalho(self, valor):
        self.cabecalho.append(valor)

    def addLinha(self, linha):
        if len(linha) != len(self.cabecalho):
            print("Tamanhos incompatíveis")
        else:
            self.dados.append(linha)

    def ordena_por(self, valor):
        index = self.cabecalho.dados.index(valor)
        self.dados.sort(key=lambda linha: linha.dados[index])

    def __str__(self):
        result = str(self.cabecalho) + "\n" + "----------------------------------------------------------" + "\n"
        for linha in self.dados:
            result += str(linha) + "\n"
        return result

    def carregar_de_arquivo(self, arquivo):
        with open(arquivo, 'r') as file:
            lines = file.readlines()

        cabecalho = [item.strip("[]'") for item in lines[0].strip().split(',')]
        self.add_cabecalho(cabecalho)

        for line in lines[1:]:
            data = [item.strip("[]'") for item in line.strip().split(',')]
            linha = Linha()
            linha.append(data)
            self.addLinha(linha)

    def writeFile(self, arquivo):
        with open(arquivo, 'w') as file:
            cabecalho_str = ",".join([f"'{item}'" for item in self.cabecalho.dados])
            file.write(f"[{cabecalho_str}]\n")

            for linha in self.dados:
                linha_obj = Linha()
                linha_obj.append(linha)
                linha_str = ",".join([f"{item}" for item in linha_obj.dados])
                file.write(f"{linha_str}\n")
