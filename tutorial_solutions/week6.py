

from math import inf
CHARACTERS = 'ACGT'


##############
# EXERCISE 2 #
##############

def init_tip(tree, tip_name, observed_nt):
    """
    Intialise a tip of a tree with the correct costs.
    At this tip node, only the observed nucleotides are possible:
    the cost of the observed nucleotide is zero, and
    the cost of any other nucleotide is infinity.
    """
    for nt in CHARACTERS:
        if nt == observed_nt:
            tree[tip_name][nt] = 0.0
        else:
            tree[tip_name][nt] = inf


##############
# EXERCISE 2 #
##############
def sankoff_calculate(c_matrix, tree, node_name):
    """
    For the specified node of the tree, calculate the minimum possible cost 
    for each nucleotide. 
    """
    # Find the min possible cost for moving to nucleotide nt1 in the current node 'node_name'
    for nt1 in CHARACTERS:
        left_costs = list()
        right_costs = list()
        left_child = tree[tree[node_name]['left']]
        right_child = tree[tree[node_name]['right']]
        
        # From each possible nucleotide 'nt2' of the left and right child nodes.
        # Use the initialized variables above to guide you.
        # Hint: We want to update tree[node_name][nt1] with the min cost value
        for nt2 in CHARACTERS:
            # nt2 is the existing value in the child node
            # c_matrix['from nt2']['to nt1']
            # Get the previous score of each nt from the left/right child nodes 
            left_costs.append(c_matrix[nt2][nt1] + left_child[nt2])
            right_costs.append(c_matrix[nt2][nt1] + right_child[nt2])

        # Find the min cost for moving from any nt2 state to our target nt1 state
        # Update the score for the current node 'node_name'
        tree[node_name][nt1] = min(left_costs) + min(right_costs)


##############
# EXERCISE 3 #
##############
for nt in CHARACTERS:
    if my_tree['root'][nt] < min_cost:
        min_nts = [nt]
        min_cost = my_tree['root'][nt]
    elif my_tree['root'][nt] == min_cost:
        min_nts.append(nt)