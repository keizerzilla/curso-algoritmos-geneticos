# Visualizando algoritmos genéticos: Problema do Caixeiro Viajante
# Artur Rodrigues Rocha Neto
# artur.rodrigues26@gmail.com

import pgzrun
import tsp_genetic_algorithm as ga

# Variáveis que controlam a janela
# O PygameZero exige que se declare esses caras
TITLE = "Caixeiro Viajante"
WIDTH = 800
HEIGHT = 600

# Variáveis do Algoritmo Genético
pop_size = 1000
num_parents = pop_size // 2
num_cities = 60

# Geração da população inicial
# 1- Como vamos usar o PygameZero pra nos ajudar a desenhar o progresso,
#    vamos fugir um pouco daquele diagrama geral.
# 2- As variáveis da população serão globais no contexto do script,
#    por isso o uso da palavra 'global' nas funções abaixo
# 3- Uma outra biblioteca gráfica necessitaria de outra forma de implementar
#    essa parte do código.
pop = ga.init(pop_size, num_cities, WIDTH, HEIGHT)
best_solution = pop[0]


def update():
    global pop
    global best_solution
    
    # Aptidão
    fit = ga.fitness(pop)
    
    # Melhor solução atual
    best_solution, best_fit = ga.best(pop, fit)
    
    # Seleção (elitismo)
    parents = ga.elitism_selection(pop, fit, num_parents)
    
    # Cruzamento (ordenado)
    children = ga.ordered_crossover(parents)
    
    # Mutação (dependente)
    mutant = ga.dependent_mutation(children, num_mutations=1)
    
    # Nova população (pais + crianças mutantes)
    pop = parents + mutant


def draw():
    global best_solution
    
    screen.fill((0, 0, 0))
    num_cities = len(best_solution)
    
    for i in range(num_cities-1):
        screen.draw.line(best_solution[i], best_solution[(i+1)], (255, 255, 255))
    
    for p in best_solution:
        screen.draw.filled_circle(p, 6, (255, 0, 0))


pgzrun.go()

