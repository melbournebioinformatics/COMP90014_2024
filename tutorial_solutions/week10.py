

import math
import time
import random
import networkx as nx 
from copy import deepcopy
from typing import Tuple

##################
### EXERCISE 1 ###
##################

def generate_neighbour(c_solution: list) -> list:
    # randomly pick which node mappings to swap
    idx1 = random.randint(0, len(c_solution)-1)
    idx2 = random.randint(0, len(c_solution)-1)
    while idx2 == idx1:
        idx2 = random.randint(0, len(c_solution)-1)
    
    # swap the mappings
    n_solution = deepcopy(c_solution)
    n_solution[idx1][1], n_solution[idx2][1] = n_solution[idx2][1], n_solution[idx1][1]
    return n_solution


##################
### EXERCISE 2 ###
##################

def acceptance(c_energy: float, n_energy: float, temp: float) -> float:
    if n_energy < c_energy:
        return 1 
    return math.exp(-(n_energy - c_energy)/temp)


##################
### EXERCISE 3 ###
##################


def simulated_annealing(R: nx.Graph, Q: nx.Graph, k_max: int=10000) -> Tuple:
    # initialise random starting state and fitness score
    c_energy = 1
    c_solution = [
        ['J', 'K'], ['I', 'A`'], ['H', 'I`'], ['G', 'H`'], ['F', 'G`'],
        ['E', 'F`'], ['D', 'E`'], ['C', 'D`'], ['B', 'C`'], ['A', 'B`'], [None, 'J`'],
    ]

    # iterate
    for k in range(k_max):
        time.sleep(0.0005)
        temp = 1 - (k/k_max)
        print(f'temp={temp:0.2f}, energy={c_energy:0.2f}', end='\r')

        # generate & assess neighbour solution
        n_solution = generate_neighbour(c_solution)
        n_energy = objective_function(n_solution, R, Q)

        # decide to jump or stay
        if acceptance(c_energy, n_energy, temp) >= random.random():
            c_energy = n_energy 
            c_solution = n_solution

    return c_energy, c_solution


