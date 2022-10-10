# phrase_genetic_algorithm.py
# Algoritmo Genético simples que tenta gerar uma frase definida como função objetivo
# Artur Rodrigues Rocha Neto
# artur.rodrigues26@gmail.com

import string
import random
import numpy as np


def init(size, phrase):
    chars = string.ascii_lowercase + " "
    phrase_len = len(phrase)
    
    pop = []
    for i in range(size):
        s = random.choices(chars, k=phrase_len)
        pop.append(s)
    
    return pop


def fitness(pop, phrase):
    fit = []
    phrase_len = len(phrase)
    
    for s in pop:
        score = 0
        for i in range(phrase_len):
            if s[i] == phrase[i]:
                score = score + 1
        
        f = score / phrase_len
        fit.append(f)
    
    return fit


def elitism_selection(pop, fit, num_parents):
    sorted_pop = [p for _, p in sorted(zip(fit, pop), reverse=True)]
    parents = sorted_pop[:num_parents]
    
    return parents


def roulette_selection(pop, fit, num_parents):
    total_fit = sum(fit)
    prob = []
    
    for f in fit:
        p = f / total_fit
        
        prob.append(p)
    
    parents = random.choices(pop, weights=prob, k=num_parents)
    
    return parents


def onecut_crossover(parents):
    children = []
    num_parents = len(parents)
    
    for i in range(num_parents):
        p1 = parents[i]
        p2 = parents[(i + 1) % num_parents]
        
        cut_point = random.choice(range(len(p1)))
        
        child = p1[:cut_point] + p2[cut_point:]
        
        children.append(child)
    
    return children


def independent_mutation(pop, rate=0.25, num_mutations=1):
    mutants = []
    chars = string.ascii_lowercase + " "
    
    for s in pop:
        chance = random.uniform(0, 1)
        
        if chance <= rate:
            for i in range(num_mutations):
                idx = list(range(len(s)))
                p1 = random.choice(idx)
                new_char = random.choice(chars)
                
                s[p1] = new_char
            
            mutants.append(s)
        else:
            mutants.append(s)
    
    return mutants


def best(pop, fit):
    sorted_pop = [(p, f) for f, p in sorted(zip(fit, pop), reverse=True)]
    
    return sorted_pop[0][0], sorted_pop[0][1]
