import pygame
import random
import math
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pylab
import time
from collections import defaultdict

# Configurações iniciais
WIDTH, HEIGHT = 800, 600
NUM_CITIES = 60
NUM_CENTERS = 10
NUM_CITIES_SERVED = NUM_CITIES/NUM_CENTERS
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.2

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
screen = pygame.display.set_mode((WIDTH + 400, HEIGHT))
pygame.display.set_caption("Algoritmo Genético - Centros de Distribuição")

# Gerar cidades com coordenadas aleatórias
cities = [(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(NUM_CITIES)]

# Função para calcular a distância euclidiana
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Função para calcular o fitness de um indivíduo
# Limita a 6 cidades por centro de distribuição
def calculate_fitness(individual):
    city_assignments = defaultdict(list)
    total_distance = 0
    for city in cities:
        distances = [(distance(city, center), idx) for idx, center in enumerate(individual)]
        distances.sort()  # Ordenar distâncias para encontrar o centro mais próximo
        for dist, idx in distances:
            if len(city_assignments[idx]) < 6:  # Limita a 6 cidades por centro
                city_assignments[idx].append(city)
                total_distance += dist
                break
    return -total_distance  # O fitness será negativo para minimizar a distância

# Função para gerar um indivíduo aleatório
def generate_individual():
    return [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_CENTERS)]

# Função de mutação
def mutate(individual):
    if random.random() < MUTATION_RATE:
        if NUM_CENTERS == 1:
            index = 0
        else:
            index = random.randint(0, NUM_CENTERS - 1)
        
        individual[index] = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    return individual

# Função de crossover
def crossover(parent1, parent2):
    if NUM_CENTERS == 1:
        split = 1
    else:
        split = random.randint(1, NUM_CENTERS - 1)
    
    child = parent1[:split] + parent2[split:]
    return child

# Inicializa a população
population = [generate_individual() for _ in range(POPULATION_SIZE)]

# Configurar o gráfico do Matplotlib
fig = pylab.figure(figsize=[4, 6])
canvas = agg.FigureCanvasAgg(fig)
ax = fig.add_subplot(111)
fitness_evolution = []

# Loop principal do algoritmo genético
running = True
generation = 0
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_q:
               running = False

    # Avaliar a fitness da população
    population_fitness = [(individual, calculate_fitness(individual)) for individual in population]
    population_fitness.sort(key=lambda x: x[1], reverse=True)  # Ordena pela melhor fitness

    # Armazena a melhor fitness para visualização
    fitness_evolution.append(population_fitness[0][1] * -1)

    # Atualizar o gráfico do Matplotlib
    ax.clear()
    ax.plot(fitness_evolution, label="Fitness")
    ax.set_title("Evolução do Fitness")
    ax.set_xlabel("Geração")
    ax.set_ylabel("Fitness")
    ax.legend()
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.buffer_rgba()
    matplotlib_surface = pygame.image.frombuffer(raw_data, canvas.get_width_height(), "RGBA")

    print(f"Generation {generation}: Best fitness = {round(population_fitness[0][1], 2)}")
    # Seleção dos melhores indivíduos
    parents = [individual for individual, _ in population_fitness[:POPULATION_SIZE // 2]]
    # Gerar nova população
    new_population = [population[0]]
    
    while len(new_population) < POPULATION_SIZE:
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)

    population = new_population

    # Visualizar a geração atual
    screen.fill((255, 255, 255))

    # Desenhar cidades
    for city in cities:
        pygame.draw.circle(screen, (0, 0, 255), city, 5)

    # Desenhar centros de distribuição e conexões
    best_individual = population_fitness[0][0]
   
    city_assignments = defaultdict(list)
    for city in cities:
        distances = [(distance(city, center), idx) for idx, center in enumerate(best_individual)]
        distances.sort()
        for dist, idx in distances:
            if len(city_assignments[idx]) < NUM_CITIES_SERVED:
                city_assignments[idx].append(city)
                pygame.draw.line(screen, VETOR_CORES[idx], city, best_individual[idx], 3)
                # pygame.draw.line(screen, (112, 112, 112), city, population_fitness[0][1], 1)
                break

    for center in best_individual:
        pygame.draw.circle(screen, (255, 0, 0), center, 8)
  
    # Desenhar o gráfico ao lado
    screen.blit(matplotlib_surface, (WIDTH, 0))

    # Atualizar a tela
    pygame.display.flip()

    generation += 1

pygame.quit()
