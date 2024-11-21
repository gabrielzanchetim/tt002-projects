from Tabela import Tabela
from Linha import Linha

class TabelaBD(Tabela):
    
    def conta(self, coluna):
        coluna_index = self.cabecalho.dados.index(coluna)
        contagem = {}

        for linha in self.dados:
            valor = linha.dados[coluna_index]
            if valor in contagem:
                contagem[valor] += 1
            else:
                contagem[valor] = 1

        resultado = Tabela()
        resultado.add_cabecalho([coluna,"numero"])

        for valor, quantidade in contagem.items():
            linha = Linha()
            linha.append([valor,quantidade])
            resultado.addLinha(linha)

        return resultado
        
    def select(self, coluna, valor):
        coluna_index = self.cabecalho.dados.index(coluna)
        resultado = Tabela()
        resultado.add_cabecalho(self.cabecalho.dados)
    
        for linha in self.dados:
            valor_coluna = linha.dados[coluna_index]
            if valor_coluna.isdigit() and int(valor_coluna) == valor:  
                resultado.addLinha(linha.dados)
            elif valor_coluna == valor:
                resultado.addLinha(linha.dados)
    
        return resultado

