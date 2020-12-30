# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 22:00:53 2020

@author: Pariya
"""

import random
import numpy as np
import networkx as nx

#coordinate of the points
coordinate = np.array([[1,2], [3,4], [11,6], [6,7], [15,20], [10,9]])

#adjacency matrix for a weighted graph
def generate_matrix(coordinate):
    info = []
    for i in range(len(coordinate)):
        for j in range(len(coordinate)) :       
            p = np.linalg.norm(coordinate[i] - coordinate[j])
            info.append(p)
    info = np.reshape(info, (len(coordinate),len(coordinate))) 
    return info
    
def random_solution(info):
    points = list(range(len(info)))
    #print(cities)
    solution = []
    for i in range(len(info)):
        randomCity = points[random.randint(0, len(points) - 1)]
        solution.append(randomCity)
        points.remove(randomCity)

    return solution

def cycle_length(info, solution):
    cycle_length = 0
    for i in range(len(solution)):
        cycle_length += info[solution[i]][solution[i - 1]]
    return cycle_length

#generate neighbors of the solution by swapping cities
def generate_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbors.append(neighbour)
    return neighbors


#find the best neighbor depending on cycle_length lenght
def best_neighbor(info, neighbors):
    best_cycle_length = cycle_length(info, neighbors[0])
    bestNeighbour = neighbors[0]
    for neighbour in neighbors:
        current_cycle_length = cycle_length(info, neighbour)
        if current_cycle_length < best_cycle_length:
            best_cycle_length = current_cycle_length
            bestNeighbour = neighbour
    return bestNeighbour, best_cycle_length


def hill_climbing(coordinate):
    info = generate_matrix(coordinate)
    current_solution = random_solution(info)
    current_cycle_length = cycle_length(info, current_solution)
    neighbors = generate_neighbors(current_solution)
    best_neighbour, best_neighbour_cycle_length = best_neighbor(info, neighbors)

    while best_neighbour_cycle_length < current_cycle_length:
        current_solution = best_neighbour
        current_cycle_length = best_neighbour_cycle_length
        neighbours = generate_neighbors(current_solution)
        best_neighbour, bestNeighbourcycle_length = best_neighbor(info, neighbours)

    return current_solution, current_cycle_length


def draw_graph(coordinate):
    final_solution = hill_climbing(coordinate)
    G = nx.DiGraph()
    temp = final_solution[0]
    G.add_nodes_from(final_solution[0])
    for i in range(1, len(final_solution[0])):
        G.add_edge(temp[i-1], temp[i])
    G.add_edge(temp[len(temp)-1], temp[0])
    color_map = []
    for node in G:
        if node == final_solution[0][0]:
            color_map.append('lime')
        else: 
            color_map.append('plum')
    nx.draw(G, with_labels = True, node_color=color_map, node_size = 1000)
    print(final_solution)
    return

    
draw_graph(coordinate)  
    
