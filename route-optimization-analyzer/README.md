# Route Optimization Analyzer

Uma extensão avançada do projeto de otimização de rotas, focada na análise de desempenho e na comparação de algoritmos.

## Funcionalidades

- Implementação de diferentes algoritmos de otimização para rotas.
- Análise de desempenho com gráficos comparativos (tempo x comprimento).
- Testes com diferentes tamanhos de problemas (10, 100, 1000 coordenadas).
- Geração de gráficos com a biblioteca **matplotlib**.

## Como Executar

1. Certifique-se de que todos os arquivos `.py` e imagens de resultado estejam no mesmo diretório.
2. Execute o arquivo principal `main.py`:
   ```bash
   python main.py
   ```

## Estrutura

- **`Coordenada.py`**: Representa pontos no plano cartesiano.
- **`Rota.py`**: Gerencia rotas e implementa cálculos básicos.
- **`main.py`**: Script principal para análise de desempenho e geração de gráficos.
- **`Resultado_10.png`**, **`Resultado_100.png`**, **`Resultado_1000.png`**: Gráficos comparativos gerados pelo projeto.
