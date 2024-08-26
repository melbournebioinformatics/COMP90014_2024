import networkx as nx
import itertools

##################
# Introduction 1 #
##################

# undirected
graphA = nx.Graph()
graphA.add_edge('A','B')
graphA.add_edge('A','C')
graphA.add_edge('B','C')
graphA.add_edge('C','D')

# directed
graphB = nx.DiGraph()
graphB.add_edge('A','B')
graphB.add_edge('A','C')
graphB.add_edge('C','B')
graphB.add_edge('C','D')
graphB.add_edge('E','C')


##############
# Exercise 1 #
##############

def degree_distribution(graph):
    """
    For the networkx graph provided, return a tuple of lists, where
    the first list gives all observed vertex degrees, and the second list gives
    the corresponding vertex counts.
    """
    
    degree_counts = {}
    
    for node in graph.nodes():
        degree = graph.degree(node)
        
        # You could skip this bit by using a defaultdict
        if degree not in degree_counts:
            degree_counts[degree] = 0
            
        degree_counts[degree] += 1
        
    print(degree_counts)
    print(degree_counts.keys())
    print(degree_counts.values())
    degrees =  list(degree_counts.keys())
    counts = list(degree_counts.values())
    
    return (degrees, counts)        


##############
# Exercise 2 #
##############

def clustering_coefficient(graph, node_label):
    """
    Calculate and return the clustering coefficient for a node in the protein-protein network.
    The clustering coefficient is the number of edges between neighbors 
    divided by the possible number of edges between neighbors.
    """

    neighbour_nodes = list(graph.neighbors(node_label))
    possible_edges = [set(x) for x in list(itertools.combinations(neighbour_nodes,2))]
    all_edges = [set(x) for x in list(graph.edges())]
    
    actual_edges = 0
    
    for edge in possible_edges:
        if edge in all_edges:
            actual_edges += 1
    
    return actual_edges / len(possible_edges)


###############
# Extension 1 #
###############

def max_clustering_coefficients(graph, x):
    """
    Write a function to collect the top 'x' nodes ranked by clustering_coefficient. 
    Return an ordered list of tuples in the format [(node, clustering_coefficient)]
    """
    node_coeffs = dict()
    for node_label in graph.nodes():
        node_coeffs[node_label] = nx.clustering(graph, node_label)
    node_coeffs_list = [(k, v) for k, v in node_coeffs.items()]
    
    return sorted(node_coeffs_list, key=lambda node_coeffs_list: node_coeffs_list[1], reverse=True)[:x]
    

###############
# Extension 2 #
###############

def bfs_reachable(source_node, target_node, graph):
    """
    For a given source node, destination node, and a graph, return True if 
    it is possible to reach the destination from the source, else False. 
    """
    if source_node == target_node:
        return True
    
    visited = [] 
    queue = [] 

    visited.append(source_node)
    queue.append(source_node)
    
    while len(queue) > 0:
        node = queue.pop(0)
        print(node, end=' \n')
        
        for neighbor in graph.neighbors(node):
            if neighbor == target_node:
                # printing out so can see order of visited nodes in queue
                print(neighbor)
                return True
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    
    return False


##################
# Short Answer 1 #
##################

"""
=== BEGIN MARK SCHEME ===
Nodes with high clustering coefficient indicate proteins which participate in protein complexes. 
This is because the binding partners of a given protein are also binding to each other. The result is a high clustering coefficient. 
=== END MARK SCHEME ===
"""

##################
# Short Answer 2 #
##################

"""
=== BEGIN MARK SCHEME ===
A high clustering coefficient indicates that the subgraph around that node is highly interconnected (dense).<br>
We can infer that this protein is likely involved in a protein complex or a signalling pathway where it is interacting with many other proteins.
In the context of disease, mutations in these proteins are likely to have a greater impact than a protein with a low clustering coefficent and hence may be good drug targets.
=== END MARK SCHEME ===
"""