import random
import math
from collections import defaultdict

class Servicos:
    def __init__(self, largura, altura, num_centros, num_cidades_atendidas, taxa_mutacao):
        self.largura = largura
        self.altura = altura
        self.num_centros = num_centros
        self.num_cidades_atendidas = num_cidades_atendidas
        self.taxa_mutacao = taxa_mutacao

    def gera_cidades(self, num_cidades):
        return [(random.randint(50, self.largura - 50), random.randint(50, self.altura - 50)) for _ in range(num_cidades)]

    def distancia(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def calcula_fitness(self, individuo, cidades):
        atribuicoes_cidade = defaultdict(list)
        distancia_total = 0
        for cidade in cidades:
            distancias = [(self.distancia(cidade, centro), idx) for idx, centro in enumerate(individuo)]
            distancias.sort()
            for dist, idx in distancias:
                if len(atribuicoes_cidade[idx]) < self.num_cidades_atendidas:
                    atribuicoes_cidade[idx].append(cidade)
                    distancia_total += dist
                    break
        return -distancia_total, atribuicoes_cidade

    def gera_individuo(self):
        return [(random.randint(0, self.largura), random.randint(0, self.altura)) for _ in range(self.num_centros)]

    def mutar(self, individuo):
        if random.random() < self.taxa_mutacao:
            indice = random.randint(0, self.num_centros - 1)
            individuo[indice] = (random.randint(0, self.largura), random.randint(0, self.altura))
        return individuo

    def crossover(self, pai1, pai2):
        corte = random.randint(1, self.num_centros - 1)
        return pai1[:corte] + pai2[corte:]
