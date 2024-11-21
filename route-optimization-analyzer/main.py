import random
from Rota import Rota
import time
from matplotlib import pyplot, pyplot as plt


class Otimizador:
    # Este é o construtor do otimizador. Você pode adicionar código aqui
    # se julgar necessário.
    def __init__(self):
        self.plt = pyplot

    # Este método de otimização já está implementado.
    # Toda vez que o comprimento for atualizado para um valor menor, é
    # necessário salvar o comprimento e o tempo gasto na função
    # para fazer o gráfico.
    # Ao final da execução, é necessário usar o matplotlib (pyplot)
    # para gerar o gráfico (comprimento X tempo).
    # Deve ser feito o mesmo para a função de otimização 'aleatório'
    # e 'otimizadorGrupo1'
    # As três séries temporais devem ser salvas em um mesmo gráfico,
    # conforme figuras 'Resultado_10x.py'
    # Seu grupo pode adicionar código nesta função se julgar necessário.
    # O mesmo para os outros dois otimizadores.
    # A linha do gráfico referente ao 'SingleSwap' deve estar em preto.
    # A linha do gráfico referente ao 'Aleatório' deve estar em verde.
    # A linha do gráfico referente ao 'otimizadorGrupo1' deve estar em azul
    # e deve ser mais grossa que a linha dos outros algoritmos.
    # Todas as linhas devem iniciar no tempo zero e terminar no tempo final.
    def singleSwap(self, rota: Rota, time_ms: int):
        # Inicia a partir de uma rota não otimizada
        rota.shuffle()
        # Tempo de entrada na função.
        tin = round(time.time() * 1000)
        # Tempo gasto na função.
        delta_ms = round(time.time() * 1000) - tin
        minComprimento = rota.comprimento()

        comprimentos = [minComprimento]
        tempos = [0]

        while (delta_ms) < time_ms:
            # atualiza delta
            delta_ms = round(time.time() * 1000) - tin
            size_rota = len(rota.coords)
            pos1 = random.randrange(0, size_rota)
            pos2 = random.randrange(0, size_rota)
            swap(rota, pos1, pos2)
            if rota.comprimento() < minComprimento:
                minComprimento = rota.comprimento()
                comprimentos.append(minComprimento)
                tempos.append(delta_ms)
            else:
                swap(rota, pos1, pos2)  # Desfazer o swap se não for melhor

        # Checa se o último tempo registrado é menor que o tempo final desejado e adiciona um ponto final
        if tempos[-1] < time_ms:
            tempos.append(time_ms)
            comprimentos.append(minComprimento)

        self.plt.plot(tempos, comprimentos, label='Single Swap', color='black')

    def aleatorio(self, rota: Rota, time_ms: int):
        # inicia a partir de uma rota não otimizada
        rota.shuffle()
        tin = round(time.time() * 1000)
        delta_ms = round(time.time() * 1000) - tin
        minComprimento = rota.comprimento()

        comprimentos = [minComprimento]
        tempos = [0]

        while delta_ms < time_ms:
            delta_ms = round(time.time() * 1000) - tin
            rotaAux = rota.copy()
            rotaAux.shuffle()
            if rotaAux.comprimento() < minComprimento:
                rota.coords = rotaAux.coords
                minComprimento = rota.comprimento()
                comprimentos.append(minComprimento)
                tempos.append(delta_ms)

        # Checa se o último tempo registrado é menor que o tempo final desejado e adiciona um ponto final
        if tempos[-1] < time_ms:
            tempos.append(time_ms)
            comprimentos.append(minComprimento)

        self.plt.plot(tempos, comprimentos, label='Aleatório', color='green')

    def otimizadorGrupo1(self, rota: Rota, time_ms: int):
        rota.shuffle()
        tin = round(time.time() * 1000)
        minComprimento = rota.comprimento()
        comprimentos = [minComprimento]
        tempos = [0]

        while round(time.time() * 1000) - tin < time_ms:
            melhorou = False

            # Laço de busca 2-opt simplificado.
            for i in range(len(rota.coords) - 1):
                for j in range(i + 2, len(rota.coords)):
                    # Verifica o tempo a cada iteração interna.
                    if round(time.time() * 1000) - tin >= time_ms:
                        break

                    # Faz a troca 2-opt
                    rotaAux = rota.copy()
                    rotaAux.coords[i:j] = reversed(rotaAux.coords[i:j])
                    comprimento_atual = rotaAux.comprimento()

                    if comprimento_atual < minComprimento:
                        rota.coords = rotaAux.coords
                        minComprimento = comprimento_atual
                        comprimentos.append(minComprimento)
                        tempos.append(round(time.time() * 1000) - tin)
                        melhorou = True
                        break  # Encerra o loop interno se houver melhoria.

                if melhorou:
                    break  # Encerra o loop externo se houver melhoria.

            # Se não houve melhoria em uma passagem completa, termina a otimização.
            if not melhorou:
                break

        # Checa se o último tempo registrado é menor que o tempo final desejado e adiciona um ponto final.
        if tempos[-1] < time_ms:
            tempos.append(time_ms)
            comprimentos.append(minComprimento)

        self.plt.plot(tempos, comprimentos, label='Felipe_Gabriel_Rian', color='blue', linewidth=2)

    # Esta função deve salvar o gráfico. A função não deve ser alterada.
    # O objetivo final é colocar vários algoritmos vindos de grupos diferentes
    # num mesmo gráfico e depois esta função irá salvar a solução com todos os gráficos.
    def salvaFigura(self, filename):
        self.plt.tight_layout()
        self.plt.legend()
        self.plt.savefig(filename)

def swap(rota: Rota, pos1: int, pos2: int):
    aux = rota.coords[pos1]
    rota.coords[pos1] = rota.coords[pos2]
    rota.coords[pos2] = aux

# Cria uma rota Vazia.
r = Rota()
# Número de coordenadas da rota
size = int(input("Digite o número de vértices:"))
# valor máximo x e y para a coordenada
r.randomCoords(size, 400)
# Cria o otimizador
opt = Otimizador()
# Tempo de otimização em ms
time_ms = int(input("Digite o tempo em ms:"))
# Otimiza por single swap
opt.singleSwap(r, time_ms)
# Otimização aleatório
opt.aleatorio(r, time_ms)
# Otimização feita por seu grupo
opt.otimizadorGrupo1(r, time_ms)

# Configuração adicional do gráfico
plt.xlabel('Tempo (ms)')
plt.ylabel('Comprimento da Rota')
plt.title('Comparação de Algoritmos de Otimização')

# Salva a figura usando a função definida na classe
opt.salvaFigura("Resultado_" + str(size) + ".png")

