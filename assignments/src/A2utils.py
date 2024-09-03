
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

def draw_generic_tree(G: nx.DiGraph) -> None:
    fig = plt.figure(1, figsize=(3.5, 3.5))
    pos = graphviz_layout(G, prog="dot")
    nx.draw_networkx_nodes(G, pos, node_color='white', node_size=700, edgecolors='black', linewidths=2)
    nx.draw_networkx_edges(G, pos, width=2, arrows=True, arrowstyle='-|>', arrowsize=10, min_target_margin=15)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
    labels = {}
    for n1, n2, data in G.edges(data=True):
        if 'label' in data:
            labels[(n1, n2)] = data['label']
    nx.draw_networkx_edge_labels(
        G, pos, font_color='red', font_size=12, 
        edge_labels=labels, rotate=False
    )
    plt.tight_layout()
    plt.show()

def draw_suffix_trie(trie: nx.DiGraph) -> None:
    fig = plt.figure(1, figsize=(6, 8))
    pos = graphviz_layout(trie, prog="dot")
    internal = [n for n in trie.nodes() if trie.out_degree(n) != 0]
    leaves = [n for n in trie.nodes() if trie.out_degree(n) == 0]
    labels = {n: trie.nodes[n]['pos'] for n in trie.nodes() if trie.out_degree(n) == 0}
    nx.draw_networkx_nodes(trie, pos, nodelist=internal, node_color='#636363', node_size=20)
    nx.draw_networkx_nodes(trie, pos, nodelist=leaves, node_color='white', node_size=300, edgecolors='black', linewidths=1)
    nx.draw_networkx_labels(trie, pos, labels=labels, font_size=10, font_family="sans-serif")
    nx.draw_networkx_edges(trie, pos, width=1, edge_color='#636363', arrows=True, arrowstyle='-|>', arrowsize=5, min_target_margin=1)
    nx.draw_networkx_edge_labels(
        trie, pos, font_color='red', font_size=14, rotate=False,
        edge_labels={e: trie.edges[e]['label'] for e in trie.edges}
    )
    plt.title('Suffix trie built from "gattaca"')
    plt.tight_layout()
    plt.show()  

def draw_evo_tree(T: nx.DiGraph) -> None:
    fig, ax = plt.subplots(figsize=(10, 10))
    pos = graphviz_layout(T, prog="dot")
    nx.draw_networkx_nodes(T, pos, node_color='#636363', node_size=1)
    labels = {n: T.nodes[n]['label'] for n in T.nodes() if T.out_degree(n) == 0}
    prev_labels = {k: v for k, v in labels.items() if not v.startswith('CASE')}
    case_labels = {k: v for k, v in labels.items() if v.startswith('CASE')}
    text1 = nx.draw_networkx_labels(T, pos, labels=prev_labels, font_size=8, font_family="sans-serif", verticalalignment='top')
    text2 = nx.draw_networkx_labels(T, pos, labels=case_labels, font_size=8,  font_color="red", font_family="sans-serif", verticalalignment='top')
    for _, t in text1.items():
        t.set_rotation('vertical')
    for _, t in text2.items():
        t.set_rotation('vertical')
    cstyle = 'bar,angle=-180,fraction=0'
    cstyle = 'angle,angleA=-90,angleB=180,rad=0'
    nx.draw_networkx_edges(T, pos, width=1, edge_color='#636363', arrowstyle='-', node_size=0, connectionstyle=cstyle, min_source_margin=0, min_target_margin=0)
    plt.tight_layout()
    plt.subplots_adjust(bottom=-0.4)
    plt.show()