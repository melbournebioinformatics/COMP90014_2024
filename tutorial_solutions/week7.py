
import networkx as nx

##############
# Exercise 1 #
##############

def get_all_kmers(reads: list[str], k: int) -> set:
    '''
    Return a set of all k-mers of length k from a set of input reads. 
    '''
    kmers = set()
    for read in reads:
        for i in range(len(read) - k + 1):
            kmer = read[i:i+k]
            kmers.add(kmer)
    return kmers
    
##############
# Exercise 2 #
##############

def build_graph(reads: list[str], k: int):
    '''
    Given a set of reads and a value k, generate & return a de Bruijn graph represented in networkx.
    Nodes are kmer-1 prefixes / suffixes, and edges represent kmers. 
    '''
    G = nx.DiGraph()
    kmers = get_all_kmers(reads, k)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        G.add_edge(prefix, suffix, label=kmer)
    return G

##############
# Exercise 3 #
##############

def extract_contig(G: nx.DiGraph) -> str:
    """
    Extract a single contig from a de Bruijn graph
    """
    contig = ''

    # get starting node
    node = [n for n in G.nodes() if G.in_degree(n) == 0][0]
    
    # get edges from this node to other nodes
    edges = list(G.out_edges(node, data=True))
    
    # while linear chain of nodes
    while len(edges) == 1:
        n1, n2, data = edges[0]
        
        # update contig sequence with kmer 
        if contig == '':
            contig += data['label']
        else:
            contig += data['label'][-1]
        
        # update current node & edges
        node = n2                                   
        edges = list(G.out_edges(node, data=True))
    
    return contig

##############
# Exercise 4 #
##############

def extract_all_contigs(G: nx.DiGraph) -> list[str]:
    """
    Extracts all contigs from a de Bruijn graph.
    """
    contigs = []

    # get starting nodes
    starting_nodes = []
    for node in G.nodes():
        # in degree == 0
        if G.in_degree(node) == 0:
            starting_nodes.append(node)
        # 2+ child nodes
        elif G.out_degree(node) > 1:
            starting_nodes += G.neighbors(node)
        # 2+ parent nodes
        elif len(list(G.predecessors(node))) > 1:
            starting_nodes.append(node)
    
    # get edges from this node to other nodes
    for node in starting_nodes:
        contig = ''
        edges = list(G.out_edges(node, data=True))
        # while linear chain of nodes
        while len(edges) == 1 and edges[0][1] not in starting_nodes:
            n1, n2, data = edges[0]
            # update contig sequence with kmer 
            if contig == '':
                contig += data['label']
            else:
                contig += data['label'][-1]
            # update current node & edges
            node = n2                                   
            edges = list(G.out_edges(node, data=True))
        
        contigs.append(contig)
    return contigs