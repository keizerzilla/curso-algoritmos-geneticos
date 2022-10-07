# tsp_genetic_algorithm.py
# Implementação de solução do problema Caixeiro Viajante usando algoritmo genético
# OBS: TSP vem do inglês 'traveling salesperson'
# Artur Rodrigues Rocha Neto
# artur.rodrigues26@gmail.com

import random
import numpy as np


def init(size, num_cities, max_width, max_height):
    cities = []
    for i in range(num_cities):
        city = [random.randint(20, max_width - 20), random.randint(20, max_height - 20)]
        cities.append(city)
    
    pop = []
    for i in range(size):
        city_copy = cities.copy()
        random.shuffle(city_copy)
        pop.append(city_copy)
    
    return pop


def fitness(pop):
    fit = []
    
    for s in pop:
        points = s + [s[0]]
        points = np.array(s)
        
        d = np.diff(points, axis=0)
        seg_dists = np.hypot(d[:,0], d[:,1])
        dist_sum = seg_dists.sum()
        
        f = 1 / (1 + np.power(dist_sum, 8))
        
        fit.append(f)
    
    return fit


def elitism_selection(pop, fit, num_parents):
    sorted_pop = [p for _, p in sorted(zip(fit, pop), reverse=True)]
    parents = sorted_pop[:num_parents]
    
    return parents


def steady_selection(pop, fit, num_parents):
    sorted_pop = [p for _, p in sorted(zip(fit, pop), reverse=True)]
    prob = np.linspace(0.5, 0.1, len(pop))
    parents = random.choices(sorted_pop, weights=prob, k=num_parents)
    
    return parents


def tournament_selection(pop, fit, num_parents):
    parents = []
    
    for i in range(num_parents):
        f1 = random.choice(list(range(len(pop))))
        f2 = random.choice(list(range(len(pop))))
        
        if fit[f1] >= fit[f2]:
            parents.append(pop[f1])
        else:
            parents.append(pop[f2])
    
    return parents


def roulette_selection(pop, fit, num_parents):
    total_fit = sum(fit)
    prob = []
    
    for f in fit:
        p = f / total_fit
        
        prob.append(p)
    
    parents = random.choices(pop, weights=prob, k=num_parents)
    
    return parents


def ordered_crossover(parents):
    children = []
    num_parents = len(parents)
    
    for i in range(num_parents):
        child1 = []
        child2 = []
        
        p1 = parents[i]
        p2 = parents[(i + 1) % num_parents]
        
        g1 = int(random.random() * len(p1))
        g2 = int(random.random() * len(p2))
        
        start_gene = min(g1, g2)
        end_gene = max(g1, g2)
        
        for i in range(start_gene, end_gene):
            child1.append(p1[i])
        
        child2 = [item for item in p2 if item not in child1]
        
        child = child1 + child2
        children.append(child)
    
    return children


def dependent_mutation(pop, rate=0.25, num_mutations=1):
    new_pop = []
    
    for s in pop:
        chance = random.uniform(0, 1)
        
        if chance <= rate:
            for i in range(num_mutations):
                idx = list(range(len(s)))
                
                p1 = random.choice(idx)
                idx.remove(p1)
                p2 = random.choice(idx)
                
                temp = s[p1]
                s[p1] = s[p2]
                s[p2] = temp
            
            new_pop.append(s)
        else:
            new_pop.append(s)
    
    return new_pop


def best(pop, fit):
    sorted_pop = [(p, f) for f, p in sorted(zip(fit, pop), reverse=True)]
    
    return sorted_pop[0][0], sorted_pop[0][1]
