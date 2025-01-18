import pygame
import random 
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pylab 
from servicos import Servicos

# Configurações iniciais
LARGURA, ALTURA = 800, 600
NUM_CIDADES = 60
NUM_CENTROS = 10
NUM_CIDADES_ATENDIDAS = NUM_CIDADES/NUM_CENTROS
TAMANHO_POPULACAO = 50 
TAXA_MUTACAO = 0.2

VETOR_CORES = [
    (106, 137, 194), (181, 66, 51), (208, 162, 169), (165, 172, 29), (92, 169, 200),
    (111, 248, 185), (217, 151, 37), (229, 106, 177), (105, 108, 76), (149, 109, 141),
    (168, 72, 53), (76, 221, 128), (148, 244, 108), (180, 120, 215), (224, 61, 103),
    (26, 89, 152), (168, 238, 84), (125, 205, 29), (108, 195, 53), (205, 113, 84),
    (249, 242, 68), (103, 119, 109), (25, 86, 217), (70, 210, 116), (69, 85, 112),
    (202, 121, 12), (4, 31, 47), (236, 131, 46), (236, 235, 80), (29, 159, 76),
    (117, 17, 237), (93, 51, 194), (136, 106, 186), (157, 141, 9), (219, 129, 28),
    (29, 173, 81), (166, 162, 95), (49, 216, 105), (2, 170, 131), (193, 255, 249),
    (129, 111, 246), (139, 147, 201), (237, 35, 97), (86, 120, 88), (166, 119, 98),
    (153, 41, 130), (233, 19, 113), (123, 205, 142), (129, 29, 162), (250, 118, 75)
]

# Inicializa o pygame
pygame.init()
tela = pygame.display.set_mode((LARGURA + 400, ALTURA))
pygame.display.set_caption("Algoritmo Genético - Centros de Distribuição")

# Instância da classe Servicos
servicos = Servicos(LARGURA, ALTURA, NUM_CENTROS, NUM_CIDADES_ATENDIDAS, TAXA_MUTACAO)
cidades = servicos.gera_cidades(NUM_CIDADES)

# Inicializa a população
populacao = [servicos.gera_individuo() for _ in range(TAMANHO_POPULACAO)]

# Configurar o gráfico do Matplotlib
fig = pylab.figure(figsize=[4, 6])
canvas = agg.FigureCanvasAgg(fig)
ax = fig.add_subplot(111)
evolucao_fitness = []

# Loop principal do algoritmo genético
executando = True
geracao = 0
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_q:
                executando = False

    # Avaliar o fitness da população e obter atribuições de cidade para a melhor solução
    fitness_populacao = []
    for individuo in populacao:
        fitness, atribuicoes = servicos.calcula_fitness(individuo, cidades)
        fitness_populacao.append((individuo, fitness))
    fitness_populacao.sort(key=lambda x: x[1], reverse=True)  # Ordena pela melhor fitness
    melhor_individuo, melhor_fitness = fitness_populacao[0]
    atribuicoes_cidade = servicos.calcula_fitness(melhor_individuo, cidades)[1]

    # Armazena o melhor fitness para visualização
    evolucao_fitness.append(-melhor_fitness)

    # Atualizar o gráfico do Matplotlib
    ax.clear()
    ax.plot(evolucao_fitness, label="Fitness")
    ax.set_title("Evolução do Fitness")
    ax.set_xlabel("Geração")
    ax.set_ylabel("Fitness")
    ax.legend()
    canvas.draw()
    renderer = canvas.get_renderer()
    dados_raw = renderer.buffer_rgba()
    superficie_matplotlib = pygame.image.frombuffer(dados_raw, canvas.get_width_height(), "RGBA")

    print(f"Geração {geracao}: Melhor fitness = {round(melhor_fitness, 2)}")
    # Seleção dos melhores indivíduos
    pais = [individuo for individuo, _ in fitness_populacao[:TAMANHO_POPULACAO // 2]]
    # Gerar nova população
    nova_populacao = [melhor_individuo]

    while len(nova_populacao) < TAMANHO_POPULACAO:
        pai1 = random.choice(pais)
        pai2 = random.choice(pais)
        filho = servicos.crossover(pai1, pai2)
        filho = servicos.mutar(filho)
        nova_populacao.append(filho)

    populacao = nova_populacao

    # Visualizar a geração atual
    tela.fill((255, 255, 255))

    # Desenhar cidades
    for cidade in cidades:
        pygame.draw.circle(tela, (0, 0, 255), cidade, 5)

    # Desenhar centros de distribuição e conexões
    for idx, centro in enumerate(melhor_individuo):
        pygame.draw.circle(tela, (255, 0, 0), centro, 8)
        for cidade in atribuicoes_cidade[idx]:
            pygame.draw.line(tela, VETOR_CORES[idx], cidade, centro, 3)

    # Desenhar o gráfico ao lado
    tela.blit(superficie_matplotlib, (LARGURA, 0))

    # Atualizar a tela
    pygame.display.flip()

    geracao += 1

pygame.quit()
