# Visualizando algoritmos genéticos: gerando uma frase
# Artur Rodrigues Rocha Neto
# artur.rodrigues26@gmail.com

import pgzrun
import phrase_genetic_algorithm as ga

TITLE = "Gerador de frase"
WIDTH = 800
HEIGHT = 240

pop_size = 50
num_parents = pop_size // 2
phrase = "amar e mudar as coisas me interessa mais"

pop = ga.init(pop_size, phrase)
best_solution = pop[0]
best_fit = 0


def update():
    global pop
    global phrase
    global best_solution
    global best_fit
    
    # Aptidão
    fit = ga.fitness(pop, phrase)
    
    # Melhor solução atual
    best_solution, best_fit = ga.best(pop, fit)
    
    # Seleção (elitismo ou roleta?)
    parents = ga.elitism_selection(pop, fit, num_parents)
    
    # Cruzamento (corte único)
    children = ga.onecut_crossover(parents)
    
    # Mutação (independente)
    mutants = ga.independent_mutation(children, num_mutations=1)
    
    # Nova população (pais + crianças mutantes)
    pop = parents + mutants


def draw():
    global best_solution
    global best_fit
    
    best_str = "".join(best_solution)
    fit_str = f"Melhor aptidão: {round(best_fit, 4):.4f}"
    
    screen.fill((0, 0, 0))
    screen.draw.text(best_str, (20, 20), fontsize=48, color=(255, 0, 0))
    screen.draw.text(fit_str, (20, 100), fontsize=48)


pgzrun.go()
